import os
from pymongo import MongoClient
from dotenv import load_dotenv
import ssl

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_URI")

# Create MongoDB client with TLS/SSL settings
client = MongoClient(
    MONGO_URI,
    tls=True,                   
    tlsAllowInvalidCertificates=False,
    ssl_cert_reqs=ssl.CERT_REQUIRED,   
    serverSelectionTimeoutMS=30000,  
    connectTimeoutMS=10000             
)

# Connect to database and collections
db = client["mental_health_chatbot"]
users_collection = db["users"]
chats_collection = db["chats"]

