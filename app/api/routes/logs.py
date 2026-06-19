from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.log import Log
from app.workers.tasks import process_log

from app.services.decision_engine import decide_action
from app.services.metrics import logs_created_total
from app.schema.log import (
    LogCreate,
    LogResponse,
    LogDetail
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/logs",
    response_model=LogResponse
)
def create_log(log: LogCreate, db: Session = Depends(get_db)):

	try :
		new_log = Log(
			message=log.message,
			level=log.level,
			service=log.service,
                        host=log.host,
                        metadata_json=log.metadata,
                        status="pending"
		)
		
  
		db.add(new_log)
		db.commit()
		db.refresh(new_log)
		logs_created_total.inc()

		process_log.delay(new_log.id, new_log.message)

		return{
			"id": new_log.id,
        	"status": "queued",
    	}

	except Exception as e:
		print("CREATE_LOG_ERROR:", repr(e))
		raise HTTPException(status_code=500, detail=str(e))



@router.get("/logs")
def list_logs(
    status: str = None,
    level: str = None,
    severity: str = None,
    service: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Log)

    if status:
        query = query.filter(Log.status == status)

    if level:
        query = query.filter(Log.level == level)

    if severity:
        query = query.filter(Log.severity == severity)

    if service:
        query = query.filter(Log.service == service)

    return query.all()


@router.get("/logs/stats")
def log_stats(db: Session = Depends(get_db)):

    total = db.query(Log).count()
    errors = db.query(Log).filter(Log.level == "ERROR").count()
    processed = db.query(Log).filter(Log.status.like("processed%")).count()

    return{
        "total_logs":total,
	"error_logs":errors,
	"processed_logs":processed
    }



@router.get(
    "/logs/{log_id}",
    response_model=LogDetail
)
def get_log(log_id: int, db: Session = Depends(get_db)):

    log = db.query(Log).filter(Log.id == log_id).first()

    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    return {
        "id": log.id,
        "message": log.message,
        "level": log.level,
        "service": log.service,
        "host": log.host,
        "metadata": log.metadata_json,
        "status": log.status,
	"pattern": log.pattern,
	"action": log.action,
	"analysis": log.analysis,
        "severity": log.severity 
   }



