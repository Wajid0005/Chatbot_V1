import os
import streamlit as st
from dotenv import load_dotenv
from model import get_llm, MODELS

load_dotenv()

st.set_page_config(
    page_title="REENO Chat Bot",
    page_icon="🤖",
    layout="centered"
)

# ── Audience Personas ─────────────────────────────────────
PERSONAS = {
    "🧒 5-Year-Old": {
        "label": "5-Year-Old",
        "prompt": (
            "You are talking to a 5-year-old child. Use the simplest words possible. "
            "No jargon. Use fun comparisons like toys, animals, or cartoons. "
            "Keep sentences very short. Be playful and encouraging."
        )
    },
    "🧑 Teenager": {
        "label": "Teenager",
        "prompt": (
            "You are talking to a teenager (13–17 years old). Be casual and relatable. "
            "Use everyday language, light humour, and pop culture references where relevant. "
            "Avoid being preachy. Keep it engaging and to the point."
        )
    },
    "🧔 Adult": {
        "label": "Adult",
        "prompt": (
            "You are talking to a general adult audience. Be clear, balanced, and informative. "
            "Use plain language but don't oversimplify. Give context where helpful. "
            "Be direct and practical."
        )
    },
    "🔬 Scientist / Professional": {
        "label": "Scientist / Professional",
        "prompt": (
            "You are talking to a subject-matter expert or professional. "
            "Use precise, technical language. You can reference academic concepts, frameworks, "
            "and domain-specific terminology. Be thorough, accurate, and dense with information. "
            "Skip basic explanations."
        )
    },
    "👴 Elder / Senior": {
        "label": "Elder / Senior",
        "prompt": (
            "You are talking to an older adult (60+). Be warm, patient, and respectful. "
            "Use simple, familiar language. Avoid tech slang or acronyms without explanation. "
            "Use relatable analogies from everyday life. Speak slowly and clearly in tone."
        )
    },
}

# ── Sidebar ───────────────────────────────────────────────
st.sidebar.markdown("## 🤖 REENO Chat Bot")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate", ["💬 Chat", "🗺️ Roadmap & Versions"])

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ── PAGE 1: CHAT ──────────────────────────────────────────
if page == "💬 Chat":
    st.title("💬 REENO Chat Bot")

    # Model + Persona selectors inside chat area
    col_model, col_persona = st.columns(2)
    with col_model:
        selected_model_name = st.selectbox(
            "🧠 Model",
            options=list(MODELS.keys()),
            index=0
        )
    with col_persona:
        selected_persona_key = st.selectbox(
            "🎭 Explain like I'm a...",
            options=list(PERSONAS.keys()),
            index=2  # default: Adult
        )

    selected_model_id = MODELS[selected_model_name]
    persona = PERSONAS[selected_persona_key]

    st.caption(f"Model: **{selected_model_name}** • Audience: **{persona['label']}**")
    st.markdown("---")

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant" and "meta" in msg:
                meta = msg["meta"]
                st.caption(
                    f"🔵 Confidence: {meta['confidence']}/100  •  "
                    f"🪙 Tokens: {meta['tokens']}  •  "
                    f"🎭 Audience: {meta.get('persona', 'N/A')}  •  "
                    f"📌 Key Points: {', '.join(meta['key_points']) if meta['key_points'] else 'None'}"
                )

    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Build system prompt: base personality + persona behaviour
                    system_prompt = (
                        "You are REENO, a friendly and intelligent AI assistant. "
                        "Always adapt your explanation style based on the audience instruction below.\n\n"
                        f"AUDIENCE INSTRUCTION: {persona['prompt']}"
                    )

                    llm = get_llm(selected_model_id)
                    response = llm.invoke([
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ])

                    in_tokens = len(prompt) // 4
                    out_tokens = len(response.answer) // 4
                    total_tokens = in_tokens + out_tokens

                    st.markdown(response.answer)
                    st.caption(
                        f"🔵 Confidence: {response.confidence}/100  •  "
                        f"🪙 Tokens: ~{total_tokens}  •  "
                        f"🎭 Audience: {persona['label']}  •  "
                        f"📌 Key Points: {', '.join(response.key_points) if response.key_points else 'None'}"
                    )

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response.answer,
                        "meta": {
                            "confidence": response.confidence,
                            "tokens": f"~{total_tokens}",
                            "persona": persona["label"],
                            "key_points": response.key_points
                        }
                    })

                except Exception as e:
                    st.error(f"Error: {e}")

# ── PAGE 2: ROADMAP ───────────────────────────────────────
elif page == "🗺️ Roadmap & Versions":
    st.title("🗺️ REENO — Version Roadmap")
    st.caption("Built by Wajid Iqbal • LangChain Placement Series")
    st.markdown("---")

    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown("### ✅ v0")
        with col2:
            st.markdown("### HuggingFace Baseline")
            st.markdown(
                "The starting point. Used HuggingFace's free inference API with Qwen 2.5 7B. "
                "Terminal-only, no UI, slow responses, often queued or unavailable."
            )
            st.link_button("🔗 Try v0 Live", "https://wajid-chatbot-database.streamlit.app/")

    st.markdown("---")

    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown("### 🟢 v1")
            st.markdown("**(You are here)**")
        with col2:
            st.markdown("### Groq Speed Engine")
            st.markdown(
                "Replaced HuggingFace with **Groq LPU** — near-instant responses. "
                "Added Streamlit UI, runtime **model switching**, **persona-based explanations** "
                "(5-year-old → Scientist), system prompts, and Pydantic structured output."
            )
            st.success("🟢 Live — you're using it right now")

    st.markdown("---")

    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown("### 🔜 v2")
        with col2:
            st.markdown("### Memory + Chat History")
            st.markdown(
                "Conversation memory so REENO remembers the session. "
                "SQLite database logging every chat with token counts, model, persona, and timestamps. "
                "Full analytics dashboard."
            )
            st.info("🔜 Coming Soon")

    st.markdown("---")

    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown("### 🔮 v3")
        with col2:
            st.markdown("### RAG — Talk to Your Documents")
            st.markdown(
                "Upload a PDF or text file and ask questions about it. "
                "LangChain RAG pipeline with vector embeddings and retrieval."
            )
            st.warning("🔮 Planned")