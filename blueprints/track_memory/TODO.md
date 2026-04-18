# Blueprint: Track B - Memory & Personalization

## The Vision
PXL should feel like a personal tutor. To do that, it needs to remember:
- The user's name.
- Their academic major.
- The context of their last 5 questions.

## Your Mission
1. **Define the Schema:** Decide how to store the data (e.g., `user_sessions.json` or a SQLite database).
2. **State Integration:** Use `st.session_state` to capture data during the chat.
3. **Persistence:** Save that data so it persists even if the user refreshes the page.
4. **Context Injection:** Modify `core/rag_engine.py` or `core/chatbot.py` to inject the user's name/context into the AI's prompt.

## Steps to Success
- [ ] Research `Streamlit Session State`.
- [ ] Create a `core/memory.py` module.
- [ ] Implement `save_user_context()` and `get_user_context()`.
- [ ] Update `BEfun.py` to greet the user by name if it's already stored!

---
*Questions? Post in the ACM Discord!*
