import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "data", "chroma_db")
DATA_PATH = os.path.join(BASE_DIR, "data", "documents.csv")