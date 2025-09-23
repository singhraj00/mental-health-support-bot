import datetime
from config.mongo_config import chats_collection

def get_user_chats(username):
    return list(chats_collection.find({"username": username}))

def create_new_chat(username, count):
    new_chat = {
        "username": username,
        "title": f"Chat {count + 1}",
        "messages": [],
        "created_at": datetime.datetime.now()
    }
    chats_collection.insert_one(new_chat)

def save_message(username, chat_title, role, content):
    chats_collection.update_one(
        {"username": username, "title": chat_title},
        {"$push": {"messages": {"role": role, "content": content}}}
    )
