import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

class ChatResponse(BaseModel):
    answer: str = Field(description="The main answer to the user's question")
    confidence: int = Field(description="Confidence score from 0 to 100", ge=0, le=100)
    key_points: List[str] = Field(description="List of 2-4 important points", min_items=0, max_items=5)

MODELS = {
    "Llama 3.3 70B (Best)": "llama-3.3-70b-versatile",
    "Llama 3.1 8B (Very Fast)": "llama-3.1-8b-instant",
    "Gemma2 9B": "gemma2-9b-it",
}

def get_llm(selected_model: str = "llama-3.1-8b-instant"):
    # Try .env first (local dev), then st.secrets (Streamlit Cloud)
    groq_key = os.getenv("GROQ_API_KEY")

    if not groq_key:
        try:
            import streamlit as st
            groq_key = st.secrets.get("GROQ_API_KEY")
        except Exception:
            pass

    if not groq_key:
        raise ValueError("❌ GROQ_API_KEY not found in .env or st.secrets!")

    llm = ChatGroq(
        model=selected_model,
        temperature=0.7,
        api_key=groq_key,
        max_tokens=1024,
    )

    return llm.with_structured_output(ChatResponse)