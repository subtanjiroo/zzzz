
from .create_docs import *
from .store_embeddings import embeddings_and_store
from .chat import ChatChain
from .Singleton import SingletonMeta



class RAG(metaclass=SingletonMeta):
    _instance = None
    def __init__(self, API_KEY="",model=""):
        self.chat = ChatChain()
        self._API_KEY = API_KEY
        self._model = model

    #chat
        #pass message

    #docs
        #path -> file
        #text, pdf,docx, csv (list column),

    def set_api_key(self,API_KEY):
        self._API_KEY = API_KEY
    def set_model(self,model):
        self._model = model


    #embedding creating
    def store_embedding_text(self,text, customer_id):
        """
            Split the given text into chunks (docs)
            Generate embeddings and store in database
            1. Generate an embedding for each chunk.
            2. Store the generated embeddings.
			
            Example Usage:
            store_embedding_text('This is a sample text','123')
        """
        customer_id = "123456"
        #split the text into chunks
        docs = create_docs_for_string(text)

        # Store the embeddings in Postgres
        embeddings_and_store(customer_id, docs)
	

    def store_embedding_pdf(self,document_id:str, pdf_path):
        """
            Split the given pdf into chunks (docs)
            Generate embeddings and store in database
            1. Generate an embedding for each chunk.
            2. Store the generated embeddings.
            
            Example Usage:
            store_embedding_pdf('123456', 'path/to/pdf')

        """
        customer_id = "123456"

        docs = create_docs_for_pdf(pdf_path)

        # Store the embeddings in Postgres
        embeddings_and_store(document_id, docs)


    def chat(self,msg:str):
        return self.chat.responsed_from_prompt(msg)
