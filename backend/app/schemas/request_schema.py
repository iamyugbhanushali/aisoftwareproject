from pydantic import BaseModel

class AgentRequest(BaseModel):
    requirement: str