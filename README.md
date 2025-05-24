# 🧠 AI Agent Suite using Ollama + Mistral

This project features a suite of AI agents powered by the [Mistral](https://ollama.com/library/mistral) model via [Ollama](https://ollama.com/), implemented in Python. It includes:

* 💬 **Conversational Bot**
* 🗣️ **Voice Assistant**
* 🌐 **Web Scraper Bot**
* 📄 **Q\&A Document Reader**

All functionalities are available in both **CLI** and **Streamlit UI** modes.

---

## 📦 Features

| Feature                  | CLI | Streamlit UI |
| ------------------------ | --- | ------------ |
| Conversational Bot       | ✅   | ✅            |
| Voice Assistant Bot      | ✅   | ✅            |
| Web Scraper Bot          | ✅   | ✅            |
| Q\&A Document Reader Bot | ✅   | ✅            |

---

## 🛠️ Setup Instructions

### 1. Prerequisites

* Python 3.8+
* [Ollama](https://ollama.com/) (Installed and running)
* Mistral model pulled locally:

  ```bash
  ollama pull mistral
  ```

### 2. Clone the Repository

```bash
[git clone https://github.com/Thiyagu-2003/AI-Agent-LLM_-Mistrial-.git]
cd ai-agent-suite
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Streamlit Installation (For UI)

```bash
pip install streamlit
```

---

## 🚀 How to Run

### 💬 Conversational Bot

* **CLI**:

  ```bash
  python bots/conversation_bot.py
  ```

* **Streamlit UI**:

  ```bash
  streamlit run ui/conversation_ui.py
  ```

---

### 🗣️ Voice Assistant

* **CLI**:

  ```bash
  python bots/voice_assistant.py
  ```

* **Streamlit UI**:

  ```bash
  streamlit run ui/voice_ui.py
  ```

> 🔈 Voice input/output handled using `speech_recognition` and `pyttsx3`.

---

### 🌐 Web Scraper Bot

* **CLI**:

  ```bash
  python bots/web_scraper.py --url "https://example.com"
  ```

* **Streamlit UI**:

  ```bash
  streamlit run ui/web_scraper_ui.py
  ```

> Scrapes a given webpage and summarizes the content using Mistral.

---

### 📄 Q\&A Document Reader

* **CLI**:

  ```bash
  python bots/qa_doc_reader.py --file sample.pdf
  ```

* **Streamlit UI**:

  ```bash
  streamlit run ui/qa_doc_ui.py
  ```

> Accepts PDFs or text files, processes them, and answers user queries based on content.

---

## 🧠 How It Works

Each bot uses Mistral through the Ollama API. The prompts are carefully engineered to guide the model for different tasks.

* **Ollama Integration**:

  ```python
  import ollama

  response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': 'Your prompt here'}])
  ```

* **Streamlit Integration**:
  UI components interact with the same core logic using clean wrappers and session state for managing conversation history.

---

## 📁 Directory Structure

```
ai-agent-suite/
│
├── bots/
│   ├── conversation_bot.py
│   ├── voice_assistant.py
│   ├── web_scraper.py
│   └── qa_doc_reader.py
│
├── ui/
│   ├── conversation_ui.py
│   ├── voice_ui.py
│   ├── web_scraper_ui.py
│   └── qa_doc_ui.py
│
├── utils/
│   ├── ollama_utils.py
│   ├── voice_utils.py
│   └── scraper_utils.py
│
├── assets/
│   └── sample.pdf
│
├── requirements.txt
└── README.md
```


---

## 📜 License

MIT License

---

## 🙌 Acknowledgments

* [Ollama](https://ollama.com/)
* [Mistral](https://mistral.ai/)
* [Streamlit](https://streamlit.io/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

---
