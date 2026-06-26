from pydantic import BaseModel


class LogResponse(BaseModel):
    id: int
    message: str
    level: str
    status: str
    pattern: str | None = None
    action: str | None = None
    analysis: str | None = None
    severity: str | None = None
