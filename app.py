import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from auth.user_auth import signup, login
from db.chat_db import get_user_chats, create_new_chat, save_message
from llm.llm_setup import initialize_llm
from llm.qa_chain import setup_qa_chain
from utils.vector_db import load_vector_db


# 🔐 Setup Encrypted Cookies
cookies = EncryptedCookieManager(
    prefix="mhcbot_",  # unique prefix for your app
    password=os.getenv("COOKIE_SECRET", "super-secret-key")  # keep this secret in production
)

if not cookies.ready():
    st.stop()


def main():
    st.set_page_config(page_title="Mental Health Chatbot", page_icon="💙", layout="wide")

    # ✅ Auto-login if cookie exists
    if "user" not in st.session_state:
        if "user" in cookies:
            st.session_state["user"] = cookies["user"]
        else:
            st.session_state["user"] = None

    # 🔒 Login / Signup Page
    if not st.session_state["user"]:
        st.title("🔒 Login / Signup")
        option = st.radio("Choose an option:", ["Login", "Signup"])
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if option == "Signup" and st.button("Create Account"):
            ok, msg = signup(username, password)
            st.success(msg) if ok else st.error(msg)

        elif option == "Login" and st.button("Login"):
            ok, msg = login(username, password)
            st.success(msg) if ok else st.error(msg)
            if ok:
                st.session_state["user"] = username
                cookies["user"] = username   # 🍪 Save cookie
                cookies.save()
                st.rerun()
        return

    # Sidebar
    with st.sidebar:
        st.title(f"👋 Welcome, {st.session_state['user']}")
        chats = get_user_chats(st.session_state["user"])
        chat_titles = [c["title"] for c in chats]
        selected_chat = st.selectbox("📂 Your Conversations:", chat_titles) if chat_titles else None

        if st.button("➕ New Chat"):
            create_new_chat(st.session_state["user"], len(chats))
            st.rerun()

        if st.button("🚪 Logout"):
            st.session_state["user"] = None
            cookies["user"] = ""   # clear cookie
            cookies.save()
            st.rerun()

    # Main Chat
    st.title("💙 Compassionate Mental Health Chatbot")
    st.write("This chatbot provides empathetic support. It does not give medical advice.")

    vector_db = load_vector_db()
    llm = initialize_llm()
    qa_chain = setup_qa_chain(vector_db, llm)

    if selected_chat:
        current_chat = [c for c in chats if c["title"] == selected_chat][0]
        for msg in current_chat["messages"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    else:
        st.info("Start a new chat from the sidebar.")

    if user_input := st.chat_input("How are you feeling today?"):
        # Display user message
        st.chat_message("user").markdown(user_input)

        # Generate assistant response
        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = qa_chain.run(user_input)

            # Stream response line by line (preserves formatting)
            for line in full_response.split("\n"):
                placeholder.markdown(line, unsafe_allow_html=True)

        # Save messages
        save_message(st.session_state["user"], selected_chat, "user", user_input)
        save_message(st.session_state["user"], selected_chat, "assistant", full_response)   


if __name__ == "__main__":
    main()
