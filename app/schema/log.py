from pydantic import BaseModel
from typing import Optional
from typing import Dict
from typing import Any

class LogCreate(BaseModel):
	message:str
	level:str = "INFO"
	service:str|None=None
	host:str|None=None
	metadata: Optional[Dict[str, Any]] = None    	

class LogResponse(BaseModel):

    id: int
    status: str

class LogDetail(BaseModel):

    id: int
    message: str
    level: str
    status: str

    service: str | None = None
    host: str | None = None

    pattern: str | None = None
    action: str | None = None
    analysis: str | None = None

    severity: str | None = None

    metadata: dict | None = None
