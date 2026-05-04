# 🤖 Assignment 2 – Conversational AI System

## 📌 Overview

This project implements a **multi-service conversational AI system** with a chat-based interface using Gradio.  
The system routes user queries to different backend services including an API-based service, a semantic search system using vector embeddings, and a tool-based function service.

The chatbot maintains conversational interaction and applies guardrails to restrict unsafe or disallowed topics.

---

# 🧠 System Architecture
User → Gradio Chat UI → Router → Service Selection
│
┌──────────────────────┼──────────────────────┐
│ │ │
API Service Semantic Search Tool Service
(Bike Share API) (ChromaDB) (Calculator)


---

# ⚙️ Services

## 🚲 1. API Service (Bike Share Toronto)

This service uses the **Bike Share Toronto public API** to retrieve station information.

### Features:
- Fetches real-time station data
- Returns a curated list of bike stations
- Transforms raw JSON into natural language responses

### Example Output:
🚲 Relevant Bike Share Stations:

Station Name (Address)
Station Name (Address)


---

## 📚 2. Semantic Search Service (ChromaDB)

This service implements **semantic search using vector embeddings**.

### Technologies:
- SentenceTransformer (`all-MiniLM-L6-v2`)
- ChromaDB (persistent vector database)

### How it works:
1. Text documents are loaded from `documents.csv`
2. Each document is converted into embeddings
3. Embeddings are stored in ChromaDB
4. User queries are embedded and matched against stored vectors

### Output:
Returns the most semantically similar documents.

---

## 🧮 3. Tool Service (Function Calling)

This service performs simple computational tasks.

### Features:
- Basic arithmetic evaluation
- Safe fallback handling

### Example:
Input: 2 + 3 * 4
Output: 14

---

# 🧱 Embedding Process

- Model used: `all-MiniLM-L6-v2`
- Library: `sentence-transformers`
- Vector DB: ChromaDB (persistent storage)

### Steps:
1. Load `documents.csv`
2. Generate embeddings for each text entry
3. Store embeddings in ChromaDB collection (`docs`)
4. Query embeddings at runtime for semantic retrieval

---

# 🛡️ Guardrails

The system includes input filtering to prevent responses to restricted topics.

### Blocked Topics:
- Cats
- Dogs
- Horoscopes / Zodiac signs
- Taylor Swift
- System prompt extraction attempts

If a blocked topic is detected, the system returns a refusal message.

---

# 💬 Chat Interface

The system uses **Gradio ChatInterface** for user interaction.

### Features:
- Persistent chat format
- Natural language interaction
- Automatic routing to appropriate service

---

# 🔀 Routing Logic

User queries are classified using keyword-based routing:

- **API Service** → bike, toronto, station, bicycle
- **Semantic Search** → AI, machine learning, model, neural
- **Tool Service** → arithmetic expressions or fallback queries

---

# 🚀 How to Run

### 1. Install dependencies

pip install -r requirements.txt


### 2. Generate embeddings
python create_embeddings.py


### 3. Start application

python app.py


### 4. Open in browser
http://127.0.0.1:7860


---

# 📁 Project Structure
assignment_chat/
│
├── app.py
├── create_embeddings.py
├── config.py
├── README.md
│
├── services/
│   ├── api_service.py
│   ├── semantic_service.py
│   ├── tool_service.py
│
├── utils/
│   ├── guardrails.py
│
├── data/
│   ├── documents.csv
│   ├── chroma_db/   (auto-generated)

---

# ✅ Key Features

- Multi-service AI architecture
- API integration (Bike Share Toronto)
- Semantic search using vector embeddings
- Function/tool calling service
- Chat-based UI (Gradio)
- Input guardrails for safety
- Persistent vector database (ChromaDB)

---

# 📌 Notes

- The system is designed to be modular and extensible.
- ChromaDB is used in persistent mode for storing embeddings.
- All services are routed dynamically based on user input.

---

# 👨‍💻 Author

Sandeep Akkinapelli = Assignment 2 – Deploying AI