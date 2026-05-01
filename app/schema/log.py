from pydantic import BaseModel


class LogCreate(BaseModel):
    message: str
    level: str = "INFO"
