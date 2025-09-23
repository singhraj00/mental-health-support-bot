import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["mental_health_chatbot"]

users_collection = db["users"]
chats_collection = db["chats"]
