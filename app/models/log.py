from sqlalchemy import Column, Integer, String, DateTime, Text, JSON, Index
from datetime import datetime, timezone
from app.db.base import Base


def utcnow():
    return datetime.now(timezone.utc)


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    level = Column(String(20), nullable=False, default="INFO", index=True)
    service = Column(String(100), index=True)
    host = Column(String(100))
    metadata_json = Column(JSON, nullable=True)
    timestamp = Column(DateTime(timezone=True), default=utcnow)
    status = Column(String(20), default="pending", index=True)
    analysis = Column(Text, nullable=True)
    pattern = Column(String(200))
    action = Column(String(500))
    severity = Column(String(20))
    created_at = Column(DateTime(timezone=True), default=utcnow, index=True)
    processed_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index("ix_logs_service_level", "service", "level"),
        Index("ix_logs_status_created", "status", "created_at"),
    )
