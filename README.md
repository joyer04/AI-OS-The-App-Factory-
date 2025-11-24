# AI-OS-The-App-Factory-
The First Generative Operating System Concept
# 🧠 AI-OS (Prototype)

> **The Operating System that codes itself.**
> Turning natural language into instant, disposable GUI applications.

## 🚀 Concept
Traditional OS requires you to find, install, and learn apps.
**AI-OS** generates the app you need, the moment you need it.

This project uses an LLM (Large Language Model) as the kernel logic, bridging the gap between user intent and system execution.

## 🌟 Key Features
* **Zero-Install Architecture:** Apps are generated on-the-fly using Python (Streamlit/Tkinter).
* **Natural Language Control:** "Delete temp files" -> Executes safe removal commands.
* **Safety Protocol:** Built-in restricted command filtering (e.g., blocks `rm -rf /`).
* **Local/Cloud Hybrid:** Supports OpenAI API (for now) and Local Llama models (experimental).

## 🛠️ How it Works
1.  **User Input:** "Make a Pomodoro timer app."
2.  **LLM Core:** Generates Python code for a GUI timer.
3.  **OS Runtime:** Executes the code instantly in a sandboxed environment.
4.  **Disposal:** Close the app, and the code vanishes (or saves if requested).

## 📦 Installation
```bash
git clone [https://github.com/YOUR_ID/Open-AI-OS.git](https://github.com/YOUR_ID/Open-AI-OS.git)
pip install -r requirements.txt
python kernel.py
