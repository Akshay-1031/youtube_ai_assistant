# 🎥 YouTube AI Assistant

An AI-powered YouTube Assistant built using **LangChain**, **Ollama (Qwen3)**, **Streamlit**, and **LCEL (LangChain Expression Language)**. The assistant intelligently uses tool calling to retrieve YouTube transcripts, metadata, thumbnails, and search results, enabling users to interact with YouTube videos through natural language.

---

## Features

-  Agentic AI workflow using LangChain
-  Dynamic tool calling with structured tools
-  Fetch YouTube transcripts
-  Retrieve video metadata
-  Retrieve video thumbnails
-  Search YouTube videos
-  Recursive tool-calling workflow using LCEL
-  Local inference using Ollama (Qwen3)
-  Interactive Streamlit web interface

---

##  Architecture

```
                    User
                      │
                      ▼
               Streamlit Interface
                      │
                      ▼
             LangChain Agent (Qwen3)
                      │
          Decides Which Tool to Call
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
 Transcript      Metadata      Search
    Tool            Tool         Tool
        │             │             │
        └─────────────┼─────────────┘
                      ▼
               Final AI Response
```

---

## Tech Stack

- Python
- LangChain
- LangChain Core (LCEL)
- Ollama
- Qwen3 8B
- Streamlit
- yt-dlp
- YouTube Transcript API
- Pytube

---

## Project Structure

```
youtube_ai_assistant/
│
├── app.py               # Streamlit frontend
├── agent.py             # LLM initialization and tool binding
├── chains.py            # Recursive agent workflow (LCEL)
├── prompts.py           # Prompt templates
├── tools.py             # Custom LangChain tools
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Akshay-1031/youtube_ai_assistant.git
cd youtube_ai_assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Install Ollama

Download Ollama

https://ollama.com/download

Pull the Qwen model

```bash
ollama pull qwen3:8b
```

Make sure the Ollama server is running

```bash
ollama serve
```

---

## ▶ Running the Application

```bash
streamlit run app.py
```

---

## Example Queries

```
Summarize this video

https://www.youtube.com/watch?v=...
```

```
Get the metadata of

https://www.youtube.com/watch?v=...
```

```
Fetch the transcript of

https://www.youtube.com/watch?v=...
```

```
Search YouTube for LangChain tutorials
```

---

## Demo

Add screenshots of the application here.

Example:

```
README Images/
    home.png
    metadata.png
    transcript.png
```

---

## Future Improvements

- AI-powered video summarization
- Chat with video transcript
- Download transcript as PDF
- Multi-language transcript support
- Conversation memory
- RAG integration for long videos
- Semantic transcript search

---

## Learning Outcomes

This project demonstrates:

- LangChain Tool Calling
- Agentic AI Workflows
- Recursive LCEL Chains
- Structured Tool Development
- Local LLM Deployment with Ollama
- Streamlit Application Development
- Integration with External APIs

---


## Author

**Venkat Akshay Grandhi**
