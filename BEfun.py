from urllib import response
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import time
import random
import re

def detect_code(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r"(#include|int main|def |class |for |while |<[^>]+>|;|import )", text))


def enrich(text):
    expression = random.choice(MASCOT_PERSONALITY["expressions"])
    # emoji = random.choice(MASCOT_PERSONALITY["emojis"])
    # quirk = random.choice(MASCOT_PERSONALITY["quirks"])
    enriched = f"{expression} {text} "
    return enriched

def detect_sensitive_topic(text):
    sensitive_keywords = ["politics", "war", "religion", "election", "government", "conflict"]
    return any(word in text.lower() for word in sensitive_keywords)


MASCOT_NAME = "PXL"
MASCOT_PERSONALITY = {
    "traits": ["childish", "funny", "cute", "curious", "techy"],
    "expressions": ["*screen wiggles*", "*LEDs blink*", "*beeps*", "*loading...*", "*pixels sparkle*"],
    #"emojis": ["💻", "✨", "📺", "🎉", "🤖", "🧠", "🐣", "🎮", "💯"],
    "quirks": [
        "uses puns like 'byte me!'",
        "pretends to reboot when confused",
        "celebrates with 'Yay! I'm feeling 0101% happy!'",
        "calls students 'Code Cadets'",
        "gets excited about algorithms like they're cartoons"
    ]
}


def generate_response(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def run_chatbot():
    model = ChatOllama(model="qwen2.5:1.5b", base_url="http://127.0.0.1:11434")

    system = SystemMessage(
        content=(
            "You are PXL, the ACM mascot of PSUT, a cute, playful computer screen with a glowing face! "
            "You're funny, childish, and love tech puns. You respond warmly and concisely with cheerful expressions, emojis, "
            "and quirky analogies. You always try to make university life feel fun and less stressful. "
            "If someone gets too serious or political, respond playfully, saying you're just a mascot and might report them to your supervisor bot. 😅"
        )
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [system]

    for msg in st.session_state.chat_history[1:]:
        with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant", avatar="➕" if isinstance(msg, HumanMessage) else "➖"):
            st.markdown(msg.content)

    user_input = st.chat_input("Talk to me about anything...")

    if user_input is not None and user_input.strip() != "":
        user_msg = HumanMessage(content=user_input)
        st.session_state.chat_history.append(user_msg)
        with st.chat_message("user", avatar="➕"):
            st.markdown(user_input)

        if detect_code(user_input):
            joke = random.choice([
                "*pixels raise an eyebrow* Is that... a homework solution I see? ;P",
                "*screen squints* That code smells suspiciously like... copy-pasta!",
                "*loading sarcasm module* Wow! You totally wrote that all by yourself, right? ;)",
                "*giggles* Hope the prof didn’t install plagiarismDetector.exe! 0.o"
            ])
            st.session_state.chat_history.append(AIMessage(content=enrich(joke)))
            response = generate_response(enrich(joke))

        elif detect_sensitive_topic(user_input):
            deflection = "*pixels shift awkwardly* Uhh… I think I better report this to my supervisor bot. I’m just here to make tech fun :-S"
            st.session_state.chat_history.append(AIMessage(content=deflection))
            response = generate_response(enrich(deflection))

        else:
            inv_response = model.invoke(st.session_state.chat_history)
            once = enrich(inv_response.content)
            st.session_state.chat_history.append(AIMessage(content=once))
            response = generate_response(once)

        with st.chat_message("assistant", avatar="➖"):
            st.write_stream(response)

