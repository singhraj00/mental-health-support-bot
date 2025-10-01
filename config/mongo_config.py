import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# Create MongoDB client using correct pymongo options
client = MongoClient(
    MONGO_URI,
    tls=True,                      # enforce TLS 1.2+
    tlsAllowInvalidCertificates=False,  # require valid certificates
    serverSelectionTimeoutMS=30000,     # 30s server selection timeout
    connectTimeoutMS=10000              # 10s connection timeout
)

# Connect to database and collections
db = client["mental_health_chatbot"]
users_collection = db["users"]
chats_collection = db["chats"]
