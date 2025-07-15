# 🧠 Multi-Agent Financial Assistant with Web + Stock Analysis

A beautiful web-based assistant built using [`Phi`](https://docs.phidata.com/) multi-agent framework, powered by LLaMA3 (via Groq), integrated with finance tools (`yfinance`) and web search (`Google`). It supports:

- Real-time stock price queries
- Financial fundamentals & news
- Web search with citations
- Markdown-rendered, chat-style UI
- Light/dark theme toggle with persistence

---

## ✨ Demo

![Multi-Agent Chat UI](https://raw.githubusercontent.com/JugalGajjar/Multi-Agent-Financial-Assistant/main/assets/demo.gif)

Demo Prompts:
```
• What is the current price of NVDA stocks?
• Tell me briefly about the analyst recommendations for the NVDA stock.
```

---

## 🔧 Features

- 🤖 **Multi-Agent Architecture** with task delegation (Finance Agent + Web Search Agent)
- 🧠 **LLaMA3-8B via Groq API** for fast, accurate language understanding
- 📈 **Real-Time Finance Tools** via `yfinance`
- 🔍 **Web Search Agent** with Google Search integration
- 🧾 **Markdown Support** in responses (tables, code, formatting)
- 🌙 **Dark/Light Mode Toggle**
- 💬 **Chat History with Markdown Rendering**
- 🧪 Built on **Flask** + **HTML** + **JS** + **CSS**

---

## 🗂 Project Structure

```
├── app.py           # Flask backend
├── agents.py        # All Phi agents defined here
├── requirements.txt # Dependencies
├── static/
│ ├── style.css      # UI styling (dark/light mode, markdown tables)
│ └── script.js      # Chat logic, markdown rendering, theme toggle
├── templates/
│ └── index.html     # Frontend HTML page
├── README.md        # Readme for GitHub
└── LICENSE          # MIT License
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/JugalGajjar/Multi-Agent-Financial-Assistant.git
cd Multi-Agent-Financial-Assistant
```

### 2. Set up environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Create .env file

You'll need your Phidata and Groq API key to use the LLaMA3 model:
```
PHI_API_KEY="PUT_YOUR_PHI_API_KEY_HERE"
GROQ_API_KEY="PUT_YOUR_GROQ_API_KEY_HERE"
```

### 4. Run the app

```py
python app.py
```
Visit 👉 http://127.0.0.1:5000

---

## 📷 Screenshots

| Light Mode | Dark Mode |
|------------|-----------|
| ![light](https://raw.githubusercontent.com/JugalGajjar/Multi-Agent-Financial-Assistant/main/assets/light-screenshot.png) | ![dark](https://raw.githubusercontent.com/JugalGajjar/Multi-Agent-Financial-Assistant/main/assets/dark-screenshot.png) |

---

## 🧩 Powered By

- [Phi](https://docs.phidata.com/) — multi-agent orchestration
- [Groq](https://console.groq.com/) — blazing fast LLM inference
- [yFinance](https://pypi.org/project/yfinance/) — real-time stock market data
- [Google](https://google.com/) — web search tool
- [Flask](https://flask.palletsprojects.com/) — web backend
- [Marked.js](https://marked.js.org/) — markdown rendering in browser

---

## 🛠 Todo / Enhancements

- [ ] Add chat history offline persistence with SQLite
- [ ] Animate typing effect for responses
- [ ] Beautify responses
- [ ] Allow export of chat as Markdown/PDF

---

## 📄 License

MIT © 2025
