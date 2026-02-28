import sqlite3
import os
import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "chat_storage.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create the messages table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            mode TEXT NOT NULL DEFAULT 'general',
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print(f"[DB] SQLite initialized at {DB_PATH}")

def insert_message(session_id: str, role: str, content: str, mode: str = "general"):
    """Insert a single message into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (session_id, role, content, mode, timestamp) VALUES (?, ?, ?, ?, ?)",
        (session_id, role, content, mode, datetime.datetime.now(datetime.timezone.utc).isoformat())
    )
    conn.commit()
    conn.close()

def get_history(session_id: str, mode: str | None = None) -> list[dict]:
    """Retrieve chat history for a session, optionally filtered by mode."""
    conn = get_connection()
    cursor = conn.cursor()
    if mode:
        cursor.execute(
            "SELECT role, content, mode, timestamp FROM messages WHERE session_id = ? AND mode = ? ORDER BY timestamp ASC",
            (session_id, mode)
        )
    else:
        cursor.execute(
            "SELECT role, content, mode, timestamp FROM messages WHERE session_id = ? ORDER BY timestamp ASC",
            (session_id,)
        )
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def get_all_sessions() -> list[dict]:
    """Get a summary of all sessions."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.session_id, 
               (SELECT content FROM messages WHERE session_id = m.session_id ORDER BY timestamp ASC LIMIT 1) as title,
               COUNT(*) as message_count, 
               MIN(timestamp) as created_at,
               MAX(timestamp) as last_active
        FROM messages m
        GROUP BY m.session_id 
        ORDER BY MAX(m.timestamp) DESC
    """)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def delete_session_messages(session_id: str):
    """Delete all messages for a session."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages WHERE session_id = ?", (session_id,))
    conn.commit()
    conn.close()

def delete_all_messages():
    """Delete all messages in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages")
    conn.commit()
    conn.close()
