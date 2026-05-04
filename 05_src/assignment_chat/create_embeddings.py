import chromadb
from sentence_transformers import SentenceTransformer
import pandas as pd
from config import DB_PATH, DATA_PATH

df = pd.read_csv(DATA_PATH)

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection("docs")

for i, row in df.iterrows():
    collection.add(
        documents=[row["text"]],
        ids=[str(i)]
    )

print("✅ Embeddings stored successfully")