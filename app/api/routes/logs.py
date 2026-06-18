from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.log import Log
from app.workers.tasks import process_log
from app.schema.log import LogCreate
from app.services.decision_engine import decide_action


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/logs")
def create_log(log: LogCreate, db: Session = Depends(get_db)):

	try :
		new_log = Log(
			message=log.message,
			level=log.level,
			status="pending"
			)
		
  
		db.add(new_log)
		db.commit()
		db.refresh(new_log)

		process_log.delay(new_log.id, new_log.message)

		return{
			"id": new_log.id,
        	"status": "queued",
    	}

	except Exception as e:
		print("CREATE_LOG_ERROR:", repr(e))
		raise HTTPException(status_code=500, detail=str(e))

@router.get("/logs")
def list_logs(status: str = None, db: Session = Depends(get_db)):

	query = db.query(Log)

	if status:
		query = query.filter(Log.status == status)

	logs = query.all()

	return logs


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



@router.get("/logs/{log_id}")
def get_log(log_id: int, db: Session = Depends(get_db)):

    log = db.query(Log).filter(Log.id == log_id).first()

    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    return {
        "id": log.id,
        "message": log.message,
        "level": log.level,
        "status": log.status,
		"pattern": log.pattern,
		"action": log.action,
		"analysis": log.analysis
    }



