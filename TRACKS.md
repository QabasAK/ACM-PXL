# PXL Build Tracks

Welcome to the PXL Build-a-thon! Instead of just "fixing bugs," we want you to ship entirely new systems. Choose a track below, follow the blueprint, and build a real AI feature.

---

## Track A: The RAG Expansion (Knowledge & Retrieval)
**Objective:** Expand PXL's knowledge beyond DSA and Algorithms.
- **Task:** Create a new RAG pipeline for a different course.
- **Blueprint:** `blueprints/track_rag/`
- **Key Skills:** Data processing, Vector Databases, Prompt Engineering.

## Track B: The "Memory" Module (State & Personalization)
**Objective:** Make PXL remember who it's talking to.
- **Task:** Implement a persistent memory system (using SQLite or a JSON-based buffer) so PXL remembers the user's name, their major, and their previous questions.
- **Blueprint:** `blueprints/track_memory/`
- **Key Skills:** State management, Database integration, Session handling.

## Track C: The Discord Integration (Multi-Platform)
**Objective:** Bring PXL to the PSUT Discord server.
- **Task:** Create a Discord bot wrapper that uses the `core/` logic to answer questions directly in a Discord channel.
- **Blueprint:** `blueprints/track_discord/`
- **Key Skills:** Discord API (discord.py), Webhooks, Async programming.

## Track D: The Analytics Dashboard (Insights)
**Objective:** Visualize what students are asking.
- **Task:** Build a hidden admin dashboard in Streamlit that shows trending questions, common topics, and AI performance metrics.
- **Blueprint:** `blueprints/track_analytics/`
- **Key Skills:** Data visualization, Pandas, Streamlit advanced layouts.

---

## How to start a track:
1.  Go to the `blueprints/` folder for your chosen track.
2.  Read the `README.md` (or the TODO comments) in that folder.
3.  Create a new folder in `pxl_modules/` for your feature.
4.  Submit a Pull Request with your working module!
