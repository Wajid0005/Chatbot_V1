import os
from dotenv import load_dotenv

print("Running Qwen File")
load_dotenv()

# Inject Streamlit secrets into environment variables if running in Streamlit
try:
    import streamlit as st
    if "HUGGINGFACEHUB_API_TOKEN" in st.secrets:
        token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = token
        os.environ["HF_TOKEN"] = token
    if "HF_TOKEN" in st.secrets:
        token = st.secrets["HF_TOKEN"]
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = token
        os.environ["HF_TOKEN"] = token
except Exception:
    pass

# Synchronize local environment variables
if os.environ.get("HUGGINGFACEHUB_API_TOKEN") and not os.environ.get("HF_TOKEN"):
    os.environ["HF_TOKEN"] = os.environ["HUGGINGFACEHUB_API_TOKEN"]
elif os.environ.get("HF_TOKEN") and not os.environ.get("HUGGINGFACEHUB_API_TOKEN"):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HF_TOKEN"]

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

api_token = os.environ.get("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=api_token
)

model = ChatHuggingFace(llm=llm)
