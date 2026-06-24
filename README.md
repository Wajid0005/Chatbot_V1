<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,50:1a0a00,100:F55027&height=200&section=header&text=REENO%20Chat%20Bot%20v1&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Groq%20Speed%20Engine%20%7C%20Persona%20Intelligence%20%7C%20Structured%20Output&descSize=15&descAlignY=60&descAlign=50" width="100%"/>

<br/>

<a href="https://wajid-chatbot-v1.streamlit.app/">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&pause=1000&color=F55027&center=true&vCenter=true&multiline=false&repeat=true&width=600&height=50&lines=%F0%9F%9F%A0+LIVE+NOW+%E2%80%94+Try+REENO+v1+%E2%86%92;Groq+LPU+%7C+Near-instant+responses+%E2%9A%A1;5+Personas+%7C+3+Models+%7C+Pydantic+Output+%F0%9F%A7%A0" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Version badges -->
<a href="https://wajid-chatbot-database.streamlit.app/">
  <img src="https://img.shields.io/badge/v0-HuggingFace_Baseline-555555?style=for-the-badge&logo=huggingface&logoColor=FFD21E"/>
</a>
<img src="https://img.shields.io/badge/v1-Groq_Edition_(YOU_ARE_HERE)-F55027?style=for-the-badge&logo=lightning&logoColor=white"/>
<img src="https://img.shields.io/badge/v2-Memory_%2B_Database-1a1a2e?style=for-the-badge&logo=sqlite&logoColor=white"/>

<br/><br/>

<!-- Tech Stack -->
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Groq_LPU-F55027?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"/>
<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

<br/><br/>

<a href="https://wajid-chatbot-v1.streamlit.app/">
  <img src="https://img.shields.io/badge/%E2%9A%A1_LAUNCH_v1_LIVE-F55027?style=for-the-badge&logoColor=white&labelColor=0d0d0d" height="42"/>
</a>
&nbsp;
<a href="https://wajid-chatbot-database.streamlit.app/">
  <img src="https://img.shields.io/badge/%F0%9F%94%B4_VIEW_v0_LIVE-555555?style=for-the-badge&logoColor=white&labelColor=0d0d0d" height="42"/>
</a>

<br/><br/>

<img src="https://img.shields.io/github/stars/Wajid0005/Chatbot-Database?style=social"/>
<img src="https://img.shields.io/github/last-commit/Wajid0005/Chatbot-Database?color=F55027"/>
<img src="https://img.shields.io/github/repo-size/Wajid0005/Chatbot-Database?color=green"/>

</div>

---

## ⚡ v0 → v1: What Actually Changed

> v0 proved the concept. v1 makes it usable.

| | v0 — HuggingFace Baseline | v1 — Groq Speed Engine |
|:--|:--|:--|
| **LLM Provider** | HuggingFace Inference API (Qwen 2.5 7B) | Groq LPU (Llama 3.3 70B / Llama 3.1 8B / Gemma2 9B) |
| **Speed** | 5–30s, often queued or down | ~0.5–2s, consistently instant |
| **Output Format** | Raw unpredictable text | Pydantic-enforced JSON (answer + confidence + key points) |
| **UI** | Terminal only | Full Streamlit web interface |
| **Model Switching** | Hardcoded, touch-the-code | Runtime dropdown, no restarts |
| **Persona System** | None | 5 audience modes (5-year-old → Scientist) |
| **System Prompt** | None — raw queries only | Defined personality + per-persona behaviour |
| **Token Counter** | tiktoken (accurate) | Estimate (chars ÷ 4) — v2 will fix this |
| **Files needed** | 6 files | 2 files (`model.py` + `streamlit_app.py`) |

---

## 🎭 The Persona System — What Makes v1 Different

Instead of a dumb question-answer loop, v1 lets you choose **who you're explaining to**. The selected persona injects a behaviour instruction directly into the system prompt before the LLM sees your question.

```
User selects: 👴 Elder / Senior
User asks: "What is an LLM?"

System prompt sent to Groq:
  "You are REENO, a friendly and intelligent AI assistant.
   AUDIENCE INSTRUCTION: You are talking to an older adult (60+).
   Be warm, patient, and respectful. Use simple, familiar language.
   Avoid tech slang or acronyms without explanation.
   Use relatable analogies from everyday life."
```

| Persona | Behaviour |
|:--------|:----------|
| 🧒 5-Year-Old | Toys, animals, cartoons. Tiny sentences. Zero jargon. |
| 🧑 Teenager | Casual, light humour, pop culture. Not preachy. |
| 🧔 Adult | Clear, balanced, practical. Default mode. |
| 🔬 Scientist / Pro | Technical, dense, domain-specific. No hand-holding. |
| 👴 Elder / Senior | Warm, patient, no acronyms, everyday analogies. |

---

## 🧠 Structured Output — Why It Matters

v0 returned raw text. You got whatever the model felt like returning — sometimes markdown, sometimes a wall of text, sometimes half-answered.

v1 forces the LLM to return a **Pydantic schema** every single time:

```python
class ChatResponse(BaseModel):
    answer: str        # The actual reply
    confidence: int    # Model's self-rating, 0–100
    key_points: List[str]  # 2–4 bullet summary
```

`llm.with_structured_output(ChatResponse)` tells LangChain to enforce this. If the model tries to return free text, it fails and retries. You always get parseable, predictable output — which means you can build UI components around it (the confidence badge, the key points expander) instead of hoping the text looks right.

---

## 🔥 Challenges & Errors I Hit

<details>
<summary><b>❌ Error 1 — "No secrets found" (st.secrets crash on local)</b></summary>
<br/>

**What happened:** Had `import streamlit as st` at the top of `model.py`. The moment Python imported the file, Streamlit tried to load `secrets.toml` — which doesn't exist locally. Crashed before `.env` even loaded.

**The fix:** Move `import streamlit as st` inside the `try` block inside `get_llm()`. Load `.env` first via `os.getenv()`, only fall back to `st.secrets` as a cloud fallback.

```python
# WRONG — crashes locally
import streamlit as st
groq_key = st.secrets.get("GROQ_API_KEY")

# RIGHT — .env first, st.secrets as fallback
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    try:
        import streamlit as st
        groq_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        pass
```

</details>

<details>
<summary><b>❌ Error 2 — ImportError: cannot import name 'get_llm' from 'model'</b></summary>
<br/>

**What happened:** `model.py` had `from model import get_llm, MODELS` inside itself — importing from its own file. Python created a circular import loop and crashed.

**The fix:** Delete that line. `model.py` is the module. It never imports from itself.

</details>

<details>
<summary><b>❌ Error 3 — KeyError: 'persona' on old chat messages</b></summary>
<br/>

**What happened:** Added `persona` to the `meta` dict mid-session. Old messages in `st.session_state` didn't have that key. Rendering history crashed with `KeyError`.

**The fix:** Use `.get()` with a fallback everywhere you read from `meta`.

```python
# WRONG
meta['persona']

# RIGHT
meta.get('persona', 'N/A')
```

</details>

<details>
<summary><b>❌ Error 4 — torchvision ModuleNotFoundError</b></summary>
<br/>

**What happened:** Old `requirements.txt` still had HuggingFace dependencies which pulled in `transformers`, which needed `torchvision`. None of these are needed in v1.

**The fix:** Strip `requirements.txt` to only what v1 actually needs:

```
streamlit
langchain
langchain-groq
pydantic
python-dotenv
pandas
```

</details>

---

## 🚀 Quickstart

```bash
# 1. Clone
git clone https://github.com/Wajid0005/Chatbot-Database.git
cd Chatbot-Database

# 2. Add your Groq API key (free at console.groq.com)
echo GROQ_API_KEY="your_key_here" > .env

# 3. Install
pip install -r requirements.txt

# 4. Run
streamlit run streamlit_app.py
```

---

## 🗂️ Project Structure

```
📦 Chatbot-Database (v1)
├── 📄 streamlit_app.py    # UI — chat interface, persona selector, roadmap page
├── 📄 model.py            # Brain — Groq + Pydantic structured output
├── 📄 requirements.txt    # Minimal v1 dependencies
└── 📄 .env                # GROQ_API_KEY (never commit this)
```

> v0 had 6 files. v1 has 2. Less code, more functionality.

---

## 🗺️ Version Roadmap

| Version | Status | What it adds |
|:--------|:-------|:-------------|
| **v0** — HuggingFace Baseline | ✅ [Live](https://wajid-chatbot-database.streamlit.app/) | Qwen 2.5 7B, terminal only, raw output |
| **v1** — Groq Speed Engine | 🟢 **You are here** | Groq LPU, personas, structured output, Streamlit UI |
| **v2** — Memory + Database | 🔜 Coming Soon | Conversation memory, SQLite logging, analytics dashboard |
| **v3** — RAG | 🔮 Planned | Upload PDFs, ask questions about your documents |

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F55027,50:1a0a00,100:0d0d0d&height=120&section=footer" width="100%"/>

**Built by Wajid Iqbal — Learning LangChain from [CampusX](https://www.youtube.com/@campusx-official)**

*v0 → v1 → v2 → ... shipping in public*

</div>