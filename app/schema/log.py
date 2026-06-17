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
