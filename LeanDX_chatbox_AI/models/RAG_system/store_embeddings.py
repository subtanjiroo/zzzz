import os

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
    



def embeddings_and_store(document_collection: str, docs: list):
    """ 
    Generate embeddings and store in database
    
    1. Generate an embedding for each chunk.
    2. Store the generated embeddings.
    
    :param pdf_id: The unique identifier for the PDF.
    :param pdf_path: The file path to the PDF.

    Example Usage:

    embeddings_and_store('123456', docs: list)
    """
    # Use text-embedding-3-small to text functional embeddings first to save cost
    # Can be improved by using more powerful embeddings like text-embedding-ada-002 or text-embedding-3-large
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    POSTGRES_DATABASE_URI = os.environ["POSTGRES_DATABASE_URI"]

    # Store the embeddings in Postgres 
    PGVector.from_documents(
        embedding=embeddings,
        documents=docs,
        collection_name=document_collection,
        connection_string=POSTGRES_DATABASE_URI,
    )