# DhandaBot Technical Guide

DhandaBot is a premium AI-driven financial advisory platform. This guide explains its architecture, persistence layer, and core features.

## 1. Architecture Overview
The project follows a decoupled client-server architecture:
- **Frontend**: Vanilla HTML5, CSS3, and JavaScript. Uses Phosphor Icons and Google Fonts (Syne & DM Sans).
- **Backend**: FastAPI (Python) serving as the API and static file server.
- **AI Engine**: Google Gemini API (via `google-generativeai`).

## 2. File Structure
```bash
/finchatbot
  /backend
    main.py         # Entry point, serves /assets and /
    router.py       # API Endpoint definitions
    chat_service.py # Gemini integration & system prompts
    database.py      # SQLite connection & query logic
    session_manager.py # Business logic for sessions
    chat_history.db  # SQLite Database (Auto-generated)
  /frontend
    index.html      # Single-page application UI
    logo.png        # DhandaBot branding asset
  pyproject.toml    # Root environment configuration
  main.py           # Root entry point wrapper
```

## 3. Persistent Chat History
DhandaBot implements a robust persistence mechanism:
1. **SQLite Core**: All messages are stored in a `messages` table in `chat_history.db`.
2. **Session IDs**: Every chat session has a unique UUID stored in the browser's `localStorage`.
3. **Descriptive Titles**: The sidebar fetches the first message of each session to use as a title, providing a ChatGPT-like experience.
4. **Hydration**: On page load, the frontend fetches the full conversation history from the `/api/history/{session_id}` endpoint.
5. **Management**: Users can delete individual sessions via the trash icon on hover, or clear all messages using the "Clear History" button.

## 4. Visualization Engine
The "Pure Yukti" feature visualizes financial data:
- **Trigger**: When asked for a budget, the AI outputs structured JSON inside `[BUDGET_JSON]` tags.
- **Parser**: The frontend JS regex-identifies these tags and removes them from the visible text.
- **Renderer**: The `renderBudgetBlock()` function converts the JSON into CSS-styled bar charts and comparative tables.
- **CSV Export**: Users can download the current session data into a formatted CSV file.

## 5. Security & Modes
- **Finance Mode**: Extends a strict system prompt to the AI, forcing it to provide professional, data-driven financial advice and refuse non-financial queries.
- **General Mode**: Operates as a helpful, broad-purpose assistant.
- **Authentication**: A simulated bank-level login modal is provided for UI/UX demonstration.

## 6. How to Run
```bash
# From the project root
uv run main.py
```
This starts the server on `http://localhost:8000`.
