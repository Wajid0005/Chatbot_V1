import os
from dotenv import load_dotenv

print("Running Qwen File")
load_dotenv()

# Inject Streamlit secrets into environment variables if running in Streamlit
try:
    import streamlit as st
    if "HUGGINGFACEHUB_API_TOKEN" in st.secrets:
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
except Exception:
    pass

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=api_token
)

model = ChatHuggingFace(llm=llm)
