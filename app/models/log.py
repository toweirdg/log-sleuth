from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import JSON
from datetime import datetime, UTC
from app.db.base import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    level = Column(String(20), nullable=False, index=True)
    service = Column(String(100), index=True)
    host = Column(String(100))
    metadata_json = Column(JSON, nullable=True)
    level = Column(String, default="INFO", index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(UTC))
    status = Column(String(20), default="pending", index=True)
    analysis = Column(String, nullable=True)
    pattern = Column(String(200))
    action = Column(String(500))
    severity = Column(String(20))
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)
    processed_at = Column(DateTime)
    

    __table_args__ = (
        Index("ix_logs_service_level", "service", "level"),
        Index("ix_logs_status_created", "status", "created_at"),
    )

