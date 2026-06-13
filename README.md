<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Wajid's%20REENO%20Chat%20Bot&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Conversational%20Engine%20%7C%20Token%20Analytics%20Dashboard&descSize=14&descAlignY=55&descAlign=50" width="100%"/>

<!-- Typing Animation -->
<a href="https://wajid-chatbot-database.streamlit.app/">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=FF4B4B&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=80&lines=%F0%9F%94%B4+LIVE+NOW+%E2%80%94+Click+to+Try+the+App!;Powered+by+Qwen+2.5+%7C+LangChain+%7C+Streamlit" alt="Typing SVG" />
</a>

<br/>

<!-- Tech Stack Badges - Animated -->
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/%F0%9F%A4%97_Hugging_Face-FFD21E?style=for-the-badge&logoColor=black"/>
<img src="https://img.shields.io/badge/Qwen_2.5_7B-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/LangGraph-FF6F00?style=for-the-badge&logo=graphql&logoColor=white"/>

<br/><br/>

<!-- Live Demo Button -->
<a href="https://wajid-chatbot-database.streamlit.app/">
  <img src="https://img.shields.io/badge/%F0%9F%9A%80_LAUNCH_LIVE_APP-FF4B4B?style=for-the-badge&logoColor=white&labelColor=1a1a2e" height="40"/>
</a>

<br/><br/>

<!-- Repo Stats -->
<img src="https://img.shields.io/github/stars/Wajid0005/Chatbot-Database?style=social"/>
<img src="https://img.shields.io/github/forks/Wajid0005/Chatbot-Database?style=social"/>
<img src="https://img.shields.io/github/last-commit/Wajid0005/Chatbot-Database?color=blue"/>
<img src="https://img.shields.io/github/repo-size/Wajid0005/Chatbot-Database?color=green"/>

</div>

---

## 📖 About This Project

> _Recently I was learning **LangGraph** from **Nitish Sir** (Owner of **[CampusX](https://www.youtube.com/@campusx-official)**) and made this project._
> _It was so amazing — I used a deployed LLM model from **Hugging Face** and turned it into a full-fledged Chat Bot with a persistent analytics dashboard!_

This app connects to the **Qwen 2.5 7B Instruct** model hosted on Hugging Face's Inference API, wraps it using **LangChain**, and tracks every interaction in a local **SQLite** database. The entire web frontend and deployment pipeline was built with **Antigravity** (an agentic AI coding assistant).

---

## 🌟 Features at a Glance

<table>
  <tr>
    <td align="center" width="50%">
      <h3>💬 Chat Bot</h3>
      <p>Real-time conversational AI powered by<br/><b>Qwen 2.5 7B Instruct</b> via LangChain</p>
      <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square"/>
    </td>
    <td align="center" width="50%">
      <h3>📊 Analytics Dashboard</h3>
      <p>Token usage charts, cost tracking,<br/>searchable logs & CSV export</p>
      <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square"/>
    </td>
  </tr>
</table>

| Feature | Description |
|:--------|:------------|
| 🤖 **LLM Chat** | Interactive chat interface with streamed AI responses |
| 🔢 **Token Counter** | Tracks input & output tokens using `tiktoken` |
| 💰 **Cost Estimation** | Estimates API costs per interaction |
| 💾 **SQLite Logging** | Persists every chat with metadata & timestamps |
| 📈 **Usage Charts** | Line & area charts for token trends over time |
| 📥 **CSV Export** | Download your full interaction history anytime |
| 🗑️ **Clear History** | One-click database cleanup from the UI |

---

## 🧠 Challenges & Journey

<details>
<summary><b>🔧 Phase 1 — Terminal Prototype</b></summary>
<br/>

The chatbot initially ran as a **CLI script**. I was expecting and debugging raw outputs directly in the terminal. This phase helped me solidify the core LangChain wrapper logic, token counting, and database insertion flow.

```
$ python app.py
Ask: What is quantum computing?
> Quantum computing is a type of computation...
```

</details>

<details>
<summary><b>🌐 Phase 2 — Streamlit Web Deployment</b></summary>
<br/>

Transitioning from CLI to a premium web application was handled by **Antigravity** (agentic AI coding companion). It generated the multi-page Streamlit layout, sidebar navigation, chat UI components, and the analytics dashboard — allowing me to focus purely on the **model connections, DB logic, and making the overall project amazing**.

The deployment to **Streamlit Community Cloud** involved resolving dependency naming (`requirement.txt` → `requirements.txt`), auto-initializing the SQLite schema, and injecting Hugging Face API secrets into the runtime environment.

</details>

---

## 🚀 Quickstart

```bash
# 1. Clone
git clone https://github.com/Wajid0005/Chatbot-Database.git
cd Chatbot-Database

# 2. Configure secrets
echo HUGGINGFACEHUB_API_TOKEN="your_token" > .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch
streamlit run streamlit_app.py
```

---

## 🗂️ Project Structure

```
📦 Chatbot-Database
├── 📄 streamlit_app.py    # Main Streamlit web application
├── 📄 model.py            # LangChain + HuggingFace model config
├── 📄 database.py         # SQLite insert operations
├── 📄 create_db.py        # Database schema initialization
├── 📄 token_counter.py    # Tiktoken-based token counter
├── 📄 view_db.py          # CLI database viewer (pandas)
├── 📄 app.py              # Original CLI chatbot script
├── 📄 requirements.txt    # Python dependencies
└── 📄 .gitignore          # Ignored files (venv, .env, .db)
```

---

<div align="center">

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

**Built with ❤️ by Wajid — Learning LangGraph from [CampusX](https://www.youtube.com/@campusx-official)**

</div>