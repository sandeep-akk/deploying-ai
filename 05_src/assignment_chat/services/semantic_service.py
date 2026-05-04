import chromadb
from sentence_transformers import SentenceTransformer
from config import DB_PATH

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection("docs")


def semantic_service(query):
    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    docs = results.get("documents", [[]])[0]

    if not docs:
        return "No relevant results found."

    return "📚 Based on documents:\n- " + "\n- ".join(docs)