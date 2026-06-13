# 🤖 Wajid's REENO Chat Bot & Analytics Dashboard

🔗 **Live Deployment:** [https://wajid-chatbot-database.streamlit.app/](https://wajid-chatbot-database.streamlit.app/)

---

## 🛠️ Tech Stack & Badges

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-FFD21E?style=for-the-badge&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 📖 Project Overview

This project was built during my journey learning **LangGraph** and AI orchestration under the mentorship of **Nitish Sir (Owner of CampusX)**. It connects a deployed Hugging Face LLM (**Qwen 2.5 7B Instruct**) with a persistent local database configuration to record user interactions, compute metrics, and display usage statistics in real time.

---

## 🌟 Key Features

- **💬 Wajid's REENO Chat Bot:** An interactive and responsive conversational interface powered by LangChain and the Qwen model.
- **📊 Token & Cost Tracker:** Automatically counts input and output tokens using `tiktoken` and calculates estimated API costs.
- **💾 SQLite Persistent Storage:** Saves query metadata (prompt, response, tokens, cost, model name, and timestamp) automatically to `chatbot.db`.
- **📈 Analytics Dashboard:** View total interactions, accumulated cost, token consumption graphs, and export database history logs as CSV format directly from the web interface.

---

## 🧠 Challenges Faced & Resolutions

1. **Initial Development (Terminal Phase):**
   Under construction, the chatbot was first running in the CLI terminal. Reading and expecting raw outputs directly in the shell helped build and debug the foundational LangChain wrapper logic.
2. **Streamlit Transition & Deployment:**
   To turn the CLI chatbot into a premium web application, **Antigravity** (my agentic AI coding companion) generated the Streamlit dashboard layout and configuration. This allowed me to focus purely on building out the model connections, DB logic, and making the overall project amazing.

---

## 🚀 Local Quickstart

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Wajid0005/Chatbot-Database.git
   cd Chatbot-Database
   ```

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_token"
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Web App:**
   ```bash
   streamlit run streamlit_app.py
   ```