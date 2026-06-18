from app.workers.celery_app import celery_app

from app.services.log_processor import (
    categorize_log,
    detect_error_patterns,
    detect_repeated_patterns
)

from app.services.ai_engine import generate_insight
from app.services.decision_engine import decide_action
from app.services.severity_engine import get_severity
from app.services.metrics import(
    processing_failures_total
)

from app.db.session import SessionLocal
from app.models.log import Log
from app.core.logger import logger

@celery_app.task
def process_log(log_id: int, message: str):

    logger.info(
        "processing_log",
        log_id=log_id,
        message=message
    )

    db = SessionLocal()

    try:
        category = categorize_log(message)
        pattern = detect_error_patterns(message)
        severity_data = get_severity(pattern)
        severity = severity_data["severity"]
        action = severity_data["action"]

        is_repeated = detect_repeated_patterns(message)

        insight = generate_insight(message, category, pattern)
        recommended_action = decide_action(category, pattern)

        if "error" in message.lower():
            status = "processed_error"
        else:
            status = "processed"

        log_entry = db.query(Log).filter(Log.id == log_id).first()

        if log_entry:
            log_entry.level = category
            log_entry.status = status
            log_entry.pattern = ", ".join(pattern) if pattern else None
            log_entry.action = action
            log_entry.analysis = insight
            log_entry.severity = severity

            db.commit()

            logger.info(
                "log_updated",
                log_id=log_id
            )

            if is_repeated:
                print(f"[ALERT] Repeated issue detected for log {log_id}")

            print(f"""
[DEBUG]
Category: {category}
Pattern: {pattern}
Action: {action}
Insight: {insight}
""")

        else:
            logger.error(
                "log_not_found",
                log_id=log_id
            )

    except Exception as e:
        db.rollback()
        logger.error(
            "celery_processing_error",
            error=str(e)
        )
        processing_failures_total.inc() 
        raise e

    finally:
        db.close()
