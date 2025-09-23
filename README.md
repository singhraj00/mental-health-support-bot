# 💙 Compassionate Mental Health Chatbot

A **Streamlit-based AI Mental Health Assistant** that provides **empathetic conversational support**.  
Built with **LangChain + Groq LLM + ChromaDB + Firestore Auth**, this chatbot helps users express their feelings safely and stores their conversations privately.  

⚠️ **Disclaimer:**  
This chatbot does **not** provide medical advice or diagnosis. If you are in crisis, please reach out to your **local helpline** immediately.  
- 🇮🇳 India: [AASRA Helpline](https://aasra.info) — **+91-9820466726**  
- 🌍 Elsewhere: Please check your local emergency numbers.  

---

## ✨ Features
- 🔐 Secure user authentication with **Firebase/Firestore**
- 💾 Persistent chat history in **Firestore**
- 🧠 Smart conversational responses with **Groq LLM (Llama 3.3-70B)**
- 📚 Contextual memory using **ChromaDB (vector search)**
- 🚨 Crisis detection — provides helpline numbers when needed
- 🎨 Clean **Streamlit UI** with sidebar chat history
- 🗂️ Professional modular folder structure

---

## 📂 Project Structure
```
mental_health_chatbot/
│── app.py # 🎨 Streamlit UI (entry point)
│── .env # 🔑 Environment variables
│── requirements.txt # 📦 Dependencies
│── firebase_keys.json # 🔐 Firebase credentials (ignored in git)
│── .gitignore # 🚫 Ignore secrets, env, cache
│
├── config/
│ ├── firebase_config.py # ⚙️ Firebase setup
│
├── auth/
│ └── user_auth.py # 🔐 Signup/Login functions
│
├── db/
│ └── chat_db.py # 💾 Chat database operations
│
├── llm/
│ ├── llm_setup.py # 🤖 LLM initialization
│ └── qa_chain.py # 🧠 QA chain with retriever
│
└── utils/
└── vector_db.py # 📚 Vector DB (Chroma) setup
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental_health_chatbot
```

## 2️⃣ Create Virtual Environment
```
python -m venv env
source env/bin/activate    # macOS/Linux
env\Scripts\activate       # Windows
```

## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

## 4️⃣ Setup Environment Variables

```
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_HUB_TOKEN=your-token
mongo_uri=
```

## 5️⃣ Firebase Keys

#### Download your Firebase Admin SDK key as firebase_keys.json and place it in the project root.
✅ Make sure .gitignore includes this file.

## 6️⃣ Run the App

```
streamlit run app.py
```

## 🖼️ Screenshots

### 🔒 Login / Signup
![Login UI](https://via.placeholder.com/600x300.png?text=Login+Page)

### 💬 Chat Interface
![Chat UI](https://via.placeholder.com/600x300.png?text=Chat+Interface)

---

## 🛠️ Tech Stack
- 🎨 **Frontend/UI:** Streamlit  
- 💾 **Database:** Firestore (chat + auth)  
- 📚 **Vector DB:** Chroma (semantic search)  
- 🤖 **LLM:** Groq API (Llama-3.3-70B)  
- 🔤 **Embeddings:** HuggingFace MiniLM  
- ⚡ **Infra:** Python + dotenv  

---

## 🤝 Contributing
Contributions are welcome! 🚀  
1. 🍴 Fork the repo  
2. 🌿 Create a feature branch (`feature/xyz`)  
3. 💾 Commit changes  
4. 🔄 Open a PR 🎉  

---

## 📜 License
This project is licensed under the **MIT License** — feel free to use and improve.

---

✨ Made with care for mental well-being 💙

