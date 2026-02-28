from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str
    mode: str = "general"  # "general" or "finance"

class ChatResponse(BaseModel):
    session_id: str
    reply: str
    timestamp: str
    mode: str

class SessionInfo(BaseModel):
    session_id: str
    message_count: int
    created_at: str

class HistoryMessage(BaseModel):
    role: str
    content: str
    mode: str
    timestamp: str
