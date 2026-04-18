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
<p align="center">
  <img src="https://github.com/user-attachments/assets/236d781a-8064-4ef4-b5b9-13845519dc63" width="49%" />
  <img src="https://github.com/user-attachments/assets/4526f953-ac9a-4cb4-b778-6d08e56299b5" width="49%" />
</p>

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

| Level                        | Track Focus                  | Goal                                                                 | Example Tasks                                                                 | Expected Outcome |
|-----------------------------|------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------|
| **Beginner**<br>First Contribution | All Tracks                   | Understand the codebase and make your first meaningful change       | • Add logging for queries<br>• Implement simple commands (`/help`, `/about`)<br>• Improve the system prompt<br>• Add input validation<br>• Small code refactor | You understand PXL + submit your **first PR** |
| **Intermediate**<br>Feature Builders | Track A & B                  | Build useful new capabilities                                       | • Implement or expand RAG for a new course<br>• Add conversation memory<br>• Better prompting techniques<br>• Integrate external APIs (events, schedules)<br>• Create a simple modular plugin | PXL gets a **real new feature** that students can use |
| **Advanced**<br>System Engineers | Track C & D                  | Make PXL production-ready and scalable                              | • Deploy as web app / API<br>• Build Discord bot integration<br>• Add user profiles or authentication<br>• Create analytics dashboard<br>• Optimize performance & caching | PXL becomes a **usable system** for many students |
| **Research / Experimental** | All Tracks (especially A & B)| Push the boundaries and generate insights                           | • Compare different LLMs<br>• Experiment with prompting & retrieval methods<br>• Build evaluation benchmarks<br>• Improve embedding quality<br>• Explore fine-tuning ideas | You create **insights** (great for research or advanced learning) |

### How to Proceed

1. Pick a track  
2. Choose **one task** (or propose your own)  
3. Build it  
4. Submit a pull request  
5. Add your name to the contributors section  

---
Built with ❤️ by the **ACM Student Chapter @ PSUT**.
Special thanks to all the student volunteers and trainers!
