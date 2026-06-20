from celery import shared_task
import structlog

from app.services.log_processor import (
    categorize_log,
    detect_error_patterns,
    detect_repeated_patterns,
)
from app.services.ai_engine import generate_insight
from app.services.decision_engine import decide_action
from app.services.severity_engine import get_severity
from app.services.metrics import processing_failures_total
from app.db.session import SessionLocal
from app.models.log import Log

logger = structlog.get_logger()


@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=5,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_backoff_max=60,
    retry_jitter=True,
)
def process_log(self, log_id: int, message: str):
    log = logger.bind(log_id=log_id, attempt=self.request.retries + 1)
    log.info("processing_log_started")

    db = SessionLocal()
    try:
        category = categorize_log(message)
        pattern = detect_error_patterns(message)
        severity_data = get_severity(pattern)
        severity = severity_data["severity"]
        action = severity_data["action"]
        is_repeated = detect_repeated_patterns(message)
        insight = generate_insight(message, category, pattern)

        status = "processed_error" if "error" in message.lower() else "processed"

        log_entry = db.query(Log).filter(Log.id == log_id).first()

        if log_entry:
            log_entry.level = category
            log_entry.status = status
            log_entry.pattern = ", ".join(pattern) if pattern else None
            log_entry.action = action
            log_entry.analysis = insight
            log_entry.severity = severity
            db.commit()

            log.info("log_processed", severity=severity, status=status)

            if is_repeated:
                log.warning("repeated_pattern_detected", log_id=log_id)
        else:
            log.error("log_not_found")

    except Exception as exc:
        db.rollback()
        processing_failures_total.inc()
        log.error("log_processing_failed", error=str(exc))
        raise self.retry(exc=exc)

    finally:
        db.close()
