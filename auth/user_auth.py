import streamlit as st
from config.mongo_config import users_collection

def signup(username, password):
    if users_collection.find_one({"username": username}):
        return False, "❌ Username already exists"
    users_collection.insert_one({"username": username, "password": password})
    return True, "✅ Account created! Please login."

def login(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        st.session_state["user"] = username
        return True, "✅ Login successful!"
    return False, "❌ Invalid username or password"
