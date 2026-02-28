from fastapi import APIRouter, HTTPException
from models import ChatRequest, ChatResponse, SessionInfo, HistoryMessage
import session_manager
import chat_service
import database
import datetime

router = APIRouter(prefix="/api")

@router.get("/health")
def health_check():
    return {"status": "ok", "service": "DhandaBot Backend"}

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    try:
        session_id = session_manager.get_or_create_session(req.session_id)
        
        # Load history from SQLite filtered by mode for context awareness
        history = session_manager.get_session_history_for_gemini(session_id, mode=req.mode)
        
        # Send to Gemini with mode-specific system prompt
        reply, _ = chat_service.send_chat_message(history, req.message, mode=req.mode)
        
        # Persist both messages to SQLite
        session_manager.save_message(session_id, "user", req.message, req.mode)
        session_manager.save_message(session_id, "assistant", reply, req.mode)
        
        return ChatResponse(
            session_id=session_id,
            reply=reply,
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            mode=req.mode
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history/{session_id}", response_model=list[HistoryMessage])
def get_history(session_id: str, mode: str | None = None):
    """Retrieve persisted chat history for a session."""
    rows = database.get_history(session_id, mode=mode)
    return [HistoryMessage(**row) for row in rows]

@router.get("/sessions")
def get_all_sessions():
    """List all stored chat sessions."""
    return database.get_all_sessions()

@router.get("/session/{session_id}", response_model=SessionInfo)
def get_session(session_id: str):
    info = session_manager.get_session_info(session_id)
    if not info:
        raise HTTPException(status_code=404, detail="Session not found")
    return SessionInfo(**info)

@router.delete("/session/{session_id}")
def delete_session(session_id: str):
    session_manager.delete_session(session_id)
    return {"status": "deleted", "session_id": session_id}

@router.delete("/sessions")
def delete_all_sessions():
    session_manager.delete_all_sessions()
    return {"status": "deleted", "message": "All sessions cleared"}
