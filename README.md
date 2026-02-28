# DhandaBot Financial AI Advisor

DhandaBot is a full-stack, AI-powered financial advisory chatbot prototype. It demonstrates a premium front-end user experience paired with a robust Python backend that leverages the Google Gemini AI to provide specialized financial guidance.

---

## 🏗️ Architecture Overview

The project is split into two main components:
1. **Frontend:** A single-page Vanilla HTML/CSS/JS application that emphasizes a premium, secure fintech aesthetic.
2. **Backend:** A FastAPI Python application that serves the frontend, manages conversation sessions, and integrates with the Google Gemini API to generate responses.

---

## 🖥️ Frontend (HTML/CSS/JS)
**Location:** `frontend/index.html`

The frontend is a self-contained web page designed to look like a high-end wealth management portal.

### 1. Typography & Theme (CSS)
- **Fonts:** Uses Google Fonts `Syne` for display (headers, brand) and `DM Sans` for readable body text.
- **Colors & Styling:** Driven entirely by CSS Variables (`--bg-base`, `--accent-primary`). It relies on a dark "Obsidian" base with "Emerald/Mint" accents to convey financial growth and security. 
- **Glassmorphism & Texture:** Uses `backdrop-filter: blur()` for floating elements (like the chat input bar) and an SVG noise filter on the body background to create a premium, un-copyable "secure" feel.

### 2. Layout Structure (HTML)
- **Sidebar (`.sidebar`):** Contains the branding, a "New Plan" button to clear the chat, an interactive history list, and a user profile card.
- **Main Area (`.main-area`):** 
  - **Top bar:** Model selector and Login button.
  - **Chat Container (`#chat-box`):** A scrollable area where messages live. It starts with a dynamic welcome message and an anchor div (`#anchor`) used for auto-scrolling. 
  - **Input Area (`.input-wrapper`):** A floating, blurred container at the bottom holding the chat text area and send button.

### 3. Interactivity (JavaScript)
- **Modals:** Simple JS functions (`openModal`, `closeModal`) toggle an `.active` class on `.modal-overlay` elements to show/hide the Login and Profile screens.
- **`clearChat()`:** Erases the chat container, clears the `dhandabot_session_id` from the browser's `localStorage`, and injects a fresh welcome message.
- **`sendMessage()`:** 
  1. Grabs user text, injects the HTML for the user's message, and auto-scrolls.
  2. Injects a temporary "Loading" animation block.
  3. Uses the browser `fetch()` API to make a `POST` request to `/api/chat`. It includes the saved `session_id` from `localStorage` (if it exists) to maintain context.
  4. Waits for the backend to respond with JSON.
  5. Removes the loading block, parses the AI's markdown response, injects the new HTML, and saves the `session_id` returned by the server.

---

## ⚙️ Backend (Python + FastAPI)
**Location:** `backend/`

The backend handles the API routing, AI prompting, and session memory. It's built with `FastAPI` and managed via `uv` (a modern Python package manager).

### 1. Application Entry (`main.py`)
- Initializes the `FastAPI` app and configures `CORSMiddleware` so the frontend can talk to it.
- **Frontend Serving:** Uses `StaticFiles` and a root route (`@app.get("/")`) to serve the `frontend/index.html` directly when you visit `http://localhost:8000/`.
- Starts the `uvicorn` development server.

### 2. Configuration (`config.py` & `.env`)
- Uses `python-dotenv` to safely load secret variables from a local `.env` file (which is specifically ignored in source control).
- Exposes a `Settings` class that provides the `GEMINI_API_KEY`, Port, and CORS settings to the rest of the app.

### 3. API Routes (`router.py` & `models.py`)
- **`models.py`:** Uses `Pydantic` to define the exact shape of incoming and outgoing JSON data. E.g., `ChatRequest` defines that a POST requires a `message` string and an optional `session_id`.
- **`router.py`:** Defines the actual web endpoints:
  - `GET /api/health`: A simple check to ensure the server is running.
  - `POST /api/chat`: The core endpoint. It takes the user's message, retrieves past history via the session manager, passes everything to the AI service, updates the history, and returns the AI's reply.
  - `GET /api/session/{id}` & `DELETE /api/session/{id}`: Utility endpoints to view or wipe out a session memory.

### 4. Memory Management (`session_manager.py`)
- Because the Gemini API natively needs to be fed the *entire* conversation history every time you ask a new question, we must store the history on the server.
- Uses a simple Python dictionary (`sessions = {}`) to store arrays of past messages, keyed by a unique UUID string (`session_id`). 
- *Note: In a production app, this dictionary would be replaced by a database (like PostgreSQL or Redis) so history isn't lost when the server restarts.*

### 5. AI Integration (`chat_service.py`)
- Initializes the `google-generativeai` SDK with your API key.
- Defines a **System Prompt** (`SYSTEM_PROMPT`). This is a hidden set of instructions given to the AI before the user ever speaks. It tells the AI:
  - Who it is ("DhandaBot, a premium AI wealth assistant").
  - What its tone should be.
  - Its **Guardrails**: It must *only* talk about finance (investments, banking, budgets) and must politely refuse to talk about non-financial topics.
- **`send_chat_message()`:** Formats our internal session history into the specific format Gemini expects (`[{"role": "user", "parts": [...]}]`), sends the request via `chat.send_message()`, and appends the new exchange to our history list.

---

## 🚀 How to Run

1. Ensure you have `uv` installed.
2. In the `backend` folder, duplicate `.env.example` -> `.env` and insert your Gemini API key.
3. Open a terminal in the `backend` folder and run:
   ```bash
   uv run main.py
   ```
4. Open `http://localhost:8000/` in your web browser.
