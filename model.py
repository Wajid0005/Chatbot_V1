import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import list

load_dotenv()

class ChatResponse(BaseModel):
    answer: str = Field(desription = "The main answer to the user's question")
    confidence: int = Field(description = "Confidence score from 0 to 100", ge=0, le=100)
    key_points: List[str] = Field(description= "List of 2-4 important points", min_item =0, max_item=5)

MODELS = {
    "Llama 3.3 70B (Best)": "llama-3.3-70b-versatile",
    "Llama 3.1 8B (Very Fast)": "llama-3.1-8b-instant",
    "Gemma2 9B": "gemma2-9b-it",
}

def get_llm(selected_model: str = "llama-3.1-8b-instant"):
    """Return Groq LLM with structured output"""

    groq_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

    if not groq_key:
        raise ValueError("❌ GROQ_API_KEY not found! Add it in .env or Streamlit Secrets.")
    
    llm = ChatGroq(
        model = selected_model,
        temperature= 0.7,
        api_key = groq_key,
        max_tokens= 1024,
    )

    structured_llm = llm.with_structured_output(ChatResponse)
    return structured_llm