# ACM-PXL: The PSUT Student Assistant

Welcome to the **ACM-PXL** repository, the mascot and AI-powered tutor for the ACM Student Chapter at Princess Sumaya University for Technology (PSUT).

 <p align="center">
   <img src="https://github.com/user-attachments/assets/cd68fd15-4a23-4972-96d8-767804f22643" alt="PXL" width=40%>
 </p>

PXL is designed to help students navigate their programming courses, answer technical questions using specialized lecture notes (RAG), and provide general advice through a playful, tech-savvy personality.

## Features
- **Course-Specific RAG:** Specialized AI assistants for Data Structures, Algorithms, Structured Programming, and more.
- **Mascot Chat:** A casual chatbot personality that loves tech puns and community interaction.
- **Academic Support:** Integrated survival guides, FAQs, and event information.
- **Student-First Design:** Built by students, for students, using open-source tools like Streamlit, Ollama, and LlamaIndex.

## Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Framework:** [LlamaIndex](https://www.llamaindex.ai/) & [LangChain](https://www.langchain.com/)
- **Local AI:** [Ollama](https://ollama.com/) (using `qwen2.5:1.5b` and `nomic-embed-text`)
- **Backend:** Python

## Getting Started

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

## Modular Architecture (Scaffolded for Builders)
This repository is designed as a **scaffold**. We've separated the "Brain" from the "Face" so you can build on top of it without breaking anything:

- `core/`: The AI logic (Chatbot, RAG engine, and model settings).
- `modules/`: Feature modules (Survival Guide, Academic Content, Training).
- `ui/`: Reusable Streamlit components.
- `knowledge_base/`: Raw documents (PDFs/MD) for the RAG system.
- `blueprints/`: Empty templates and guides for the **Build Tracks**.

## 🤝 The PXL Build Tracks
We've defined 4 major tracks for ACM students to build:

- **Track A: RAG Expansion** (Add new courses to PXL's knowledge).
- **Track B: Memory & Personalization** (Make PXL remember users).
- **Track C: Discord Integration** (Bring PXL to the ACM server).
- **Track D: Analytics Dashboard** (See what students are asking).

Pick a track based on your experience level.  
Each track contains **clear, actionable tasks**, you are expected to build and submit a contribution.

#### Beginner — First Contribution

**Goal:** Understand the system and make your first meaningful change.

**Tasks:**
- Add logging to track user queries and responses
- Implement a new simple command (e.g., `/help`, `/about`, `/events`)
- Improve or restructure the prompt for better responses
- Add input validation or error handling
- Refactor a small part of the code for clarity

**Expected Outcome:**
- You understand how PXL works
- You submit your first PR

#### Intermediate — Feature Builders

**Goal:** Build real functionality that improves the assistant.

**Tasks:**
- Implement **RAG (Retrieval-Augmented Generation)** using a small dataset (e.g., ACM FAQs, course notes)
- Add **conversation memory** (store and reuse previous interactions)
- Improve response quality using better prompting strategies
- Integrate an external API (e.g., events, schedules, announcements)
- Design a simple modular extension (plug-in style feature)

**Expected Outcome:**
- PXL gains a meaningful new capability
- Your contribution affects real usage

#### Advanced — System Engineers

**Goal:** Turn PXL into a deployable, scalable system.

**Tasks:**
- Deploy PXL as a web app or API
- Integrate with a platform (e.g., Discord bot, web interface)
- Implement user authentication or profiles
- Build an analytics system (track usage, queries, engagement)
- Optimize performance (latency, caching, efficiency)

**Expected Outcome:**
- PXL becomes a real, usable system
- Your work impacts multiple users

#### Research / Experimental — Push the Boundaries

**Goal:** Explore advanced ideas and improve system intelligence.

**Tasks:**
- Experiment with different prompting techniques and evaluate results
- Compare multiple LLMs and analyze performance differences
- Implement embedding-based retrieval improvements
- Evaluate response accuracy and design benchmarks
- Explore fine-tuning or domain adaptation approaches

**Expected Outcome:**
- You generate insights, not just features
- Your work can evolve into research or advanced systems work


#### How to Proceed

1. Pick a track  
2. Choose **one task** (or propose your own)  
3. Build it  
4. Submit a pull request  
5. Add your name to the contributors section  

---
Built with ❤️ by the **ACM Student Chapter @ PSUT**.
Special thanks to all the student volunteers and trainers!
