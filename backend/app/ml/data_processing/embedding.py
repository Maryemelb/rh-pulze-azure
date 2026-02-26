from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from sklearn.preprocessing import normalize
import numpy as np

import chromadb
import os
from chromadb.config import Settings

db_path = os.getenv("CHROMA_PATH", "backend/app/data/embedding_db")
os.makedirs(db_path, exist_ok=True)
client = chromadb.PersistentClient(
        path=db_path,
        settings=Settings(allow_reset=True)
    )
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
collection_vect = client.get_or_create_collection(
        name="embedding_db"
    )

def generate_embeddings(df):
    columns = ['Job Description']
    texts = df[columns].fillna("").apply(lambda row: " ".join([" ".join(x) if isinstance(x, list) else str(x) for x in row]), axis=1).tolist()
    all_vectors=[]
    batch_size = 128 
    print('start3')
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        print('start')
        batch_vectors = embedding_model.embed_documents(batch_texts)
        
        # Normalize only 
        batch_vectors = normalize(np.array(batch_vectors), norm="l2")
        
        batch_ids = [str(j) for j in range(i, i+len(batch_texts))]

        all_vectors.extend(batch_vectors)

        collection_vect.add(
            documents=batch_texts,
            embeddings=batch_vectors.tolist(),
            ids=batch_ids
        )
        print(batch_vectors)
        print(f"Processed up to row {i + len(batch_texts)}")
    # add vectors to df
    # df['description_vect']= [ vec.tolist() for vec in all_vectors]
    return np.vstack(all_vectors).astype(np.float32)

