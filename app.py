import streamlit as st
from auth.user_auth import signup, login
from db.chat_db import get_user_chats, create_new_chat, save_message
from llm.llm_setup import initialize_llm
from llm.qa_chain import setup_qa_chain
from utils.vector_db import load_vector_db

def main():
    st.set_page_config(page_title="Mental Health Chatbot", page_icon="💙", layout="wide")

    if "user" not in st.session_state:
        st.session_state["user"] = None

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
            if ok: st.rerun()
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
        st.chat_message("user").markdown(user_input)
        with st.chat_message("assistant"):
            placeholder, full_response = st.empty(), ""
            for chunk in qa_chain.run(user_input).split():
                full_response += chunk + " "
                placeholder.markdown(full_response)
        save_message(st.session_state["user"], selected_chat, "user", user_input)
        save_message(st.session_state["user"], selected_chat, "assistant", full_response)

if __name__ == "__main__":
    main()
