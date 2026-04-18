# 🤖 ACM-PXL: The PSUT Student Assistant

Welcome to the official repository for **ACM-PXL**, the mascot and AI-powered tutor for the ACM Student Chapter at Princess Sumaya University for Technology (PSUT).

PXL is designed to help students navigate their programming courses, answer technical questions using specialized lecture notes (RAG), and provide general advice through a playful, tech-savvy personality.

## ✨ Features
- **Course-Specific RAG:** Specialized AI assistants for Data Structures, Algorithms, Structured Programming, and more.
- **Mascot Chat:** A casual chatbot personality that loves tech puns and community interaction.
- **Academic Support:** Integrated survival guides, FAQs, and event information.
- **Student-First Design:** Built by students, for students, using open-source tools like Streamlit, Ollama, and LlamaIndex.

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Framework:** [LlamaIndex](https://www.llamaindex.ai/) & [LangChain](https://www.langchain.com/)
- **Local AI:** [Ollama](https://ollama.com/) (using `qwen2.5:1.5b` and `nomic-embed-text`)
- **Backend:** Python

## 🚀 Getting Started

### 1. Install Ollama
Download and install [Ollama](https://ollama.com/) for your OS.

### 2. Pull the Models
Open your terminal and run:
```bash
ollama pull qwen2.5:1.5b
ollama pull nomic-embed-text
```

### 3. Clone and Install
```bash
git clone https://github.com/QabasAK/ACM-PXL.git
cd ACM-PXL
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run Frontend.py
```

## 🏗️ Modular Architecture (Scaffolded for Builders)
This repository is designed as a **scaffold**. We've separated the "Brain" from the "Face" so you can build on top of it without breaking anything:

- `core/`: The AI logic (Chatbot, RAG engine, and model settings).
- `modules/`: Feature modules (Survival Guide, Academic Content, Training).
- `ui/`: Reusable Streamlit components.
- `knowledge_base/`: Raw documents (PDFs/MD) for the RAG system.
- `blueprints/`: Empty templates and guides for the **Build Tracks**.

## 🤝 The PXL Build Tracks
Don't just fix bugs—ship a whole new system! We've defined 4 major tracks for ACM students to build:

- **📍 Track A: RAG Expansion** (Add new courses to PXL's knowledge).
- **🧠 Track B: Memory & Personalization** (Make PXL remember users).
- **📡 Track C: Discord Integration** (Bring PXL to the PSUT server).
- **📊 Track D: Analytics Dashboard** (See what students are asking).

Check out **[TRACKS.md](TRACKS.md)** to pick your mission!

---
Built with ❤️ by the **ACM Student Chapter @ PSUT**.
Special thanks to all the student volunteers and trainers!
