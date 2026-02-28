import uuid
import datetime
import database

def get_or_create_session(session_id: str | None) -> str:
    """Return existing session_id or create a new one."""
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id

def get_session_history_for_gemini(session_id: str, mode: str | None = None) -> list:
    """Load history from SQLite and format it for the Gemini chat API."""
    rows = database.get_history(session_id, mode=mode)
    history = []
    for row in rows:
        gemini_role = "model" if row["role"] == "assistant" else row["role"]
        history.append({"role": gemini_role, "parts": [row["content"]]})
    return history

def save_message(session_id: str, role: str, content: str, mode: str = "general"):
    """Persist a single message to SQLite."""
    database.insert_message(session_id, role, content, mode)

def delete_session(session_id: str):
    database.delete_session_messages(session_id)

def delete_all_sessions():
    database.delete_all_messages()

def get_session_info(session_id: str) -> dict | None:
    rows = database.get_history(session_id)
    if not rows:
        return None
    return {
        "session_id": session_id,
        "message_count": len(rows),
        "created_at": rows[0]["timestamp"]
    }
