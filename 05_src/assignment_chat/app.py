import gradio as gr

from services.api_service import api_service
from services.semantic_service import semantic_service
from services.tool_service import tool_service
from utils.guardrails import guardrails


def route(query):
    q = query.lower()

    # Service 1 — Bike Share Toronto (flexible matching)
    if any(word in q for word in [
        "bike", "bikes", "bike share", "bikeshare", "station", "bicycle", "to bike", "toronto bike"
    ]):
        return api_service(query)

    # Service 2 — Semantic search
    elif any(word in q for word in ["machine", "learning", "ai", "model"]):
        return semantic_service(query)

    # Service 3 — Tool
    else:
        return tool_service(query)


def chat(user_input, history):
    block = guardrails(user_input)
    if block:
        return block

    response = route(user_input)

    return " Assistant: " + response


gr.ChatInterface(chat).launch()