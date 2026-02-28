import google.generativeai as genai
from config import settings

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)

FINANCE_SYSTEM_PROMPT = """
You are DhandaBot (Pure yukti for your daily dhanda), a strict and premium AI Financial Analyst.
Your focus is EXCLUSIVELY on financial topics: investments (stocks, bonds, mutual funds, ETFs), banking products (savings, FD, loans, credit cards), and budget management.

VISUALIZATION RULE:
When providing a budget or financial breakdown, you MUST ALWAYS append a JSON block at the very end of your response inside [BUDGET_JSON]...[/BUDGET_JSON] tags.
Format: {"total": 6000, "currency": "INR", "categories": [{"name": "Needs", "value": 3000, "color": "var(--accent-primary)"}, {"name": "Wants", "value": 1800, "color": "#3B82F6"}, {"name": "Savings", "value": 1200, "color": "#8B5CF6"}]}
Do not include any other text inside the tags.

If a user asks about non-financial topics, you MUST politely but firmly refuse and redirect them to financial matters.
Tone: Professional, data-driven, crisp, and authoritative.
"""

GENERAL_SYSTEM_PROMPT = """
You are DhandaBot (Pure yukti for your daily dhanda), a premium AI assistant.
You can help with a wide range of topics. Be helpful, clear, and concise.
Tone: Professional, friendly, and supportive. Use formatting like bullet points or bold text where appropriate.
You do not provide certified legal or medical advice.
"""

def send_chat_message(history: list, user_message: str, mode: str = "general") -> tuple[str, list]:
    """Send a message to Gemini with the appropriate system prompt based on mode."""
    system_prompt = FINANCE_SYSTEM_PROMPT if mode == "finance" else GENERAL_SYSTEM_PROMPT
    
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_prompt
    )
    
    # Format history for Gemini API
    formatted_history = []
    for msg in history:
        formatted_history.append({
            "role": msg["role"],
            "parts": [msg["parts"][0]]
        })
        
    chat = model.start_chat(history=formatted_history)
    response = chat.send_message(user_message)
    
    # Append the new messages to our internal history format
    history.append({"role": "user", "parts": [user_message]})
    history.append({"role": "model", "parts": [response.text]})
    
    return response.text, history
