from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import JSON
from datetime import datetime, UTC
from app.db.base import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    service = Column(String, nullable=True)
    host = Column(String, nullable=True)
    metadata_json = Column(JSON, nullable=True)
    level = Column(String, default="INFO")
    timestamp = Column(DateTime, default=lambda: datetime.now(UTC))
    status = Column(String, default="pending")
    analysis = Column(String, nullable=True)
    pattern = Column(String, nullable=True)
    action = Column(String, nullable=True)
    severity = Column(String, nullable=True)
    
