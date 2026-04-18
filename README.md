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

## 🤝 How to Contribute (Student Initiative!)
We're looking for **Code Cadets** to help PXL grow! Whether you're a beginner or a pro, there's a place for you.

### Knowledge Contributions
- **Lecture Summaries:** Help PXL learn better by adding clean, high-quality Markdown or PDF summaries of your lectures to the `DSA RAG` or `Algo RAG` folders.
- **Bug Squashing:** Found a weird response? Report it or fix the RAG prompt in `ask.py`.

### Code Contributions
- **UI Enhancements:** Make PXL look even cooler with Streamlit CSS magic.
- **Personality Quirks:** Add more puns and mascot expressions to `BEfun.py`.
- **New Courses:** Help us expand to other courses!

### Design & Content
- **Survival Guide:** Add more tips for surviving PSUT to `SurvGuide.py`.
- **FAQs:** Keep the `FAQ` section in `Frontend.py` updated.

---
Built with ❤️ by the **ACM Student Chapter @ PSUT**.
Special thanks to all the student volunteers and trainers!
