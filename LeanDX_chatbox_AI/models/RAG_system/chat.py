

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector


import os
import logging

class ChatChain:
    def __init__(self):
        api_key = os.environ["OPENAI_API_KEY"]
        self.llm = ChatOpenAI(
            api_key=api_key,
            model="gpt-4o-mini",
            max_tokens=1000,
            temperature=0.5
        )
    def responsed_from_prompt(self, prompt):
        final_response = ""
        try:
            POSTGRES_DATABASE_URI = os.environ["POSTGRES_DATABASE_URI"]
            
            # Embedding model
            embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
            
            # Create a new PGVector instance: input_text will be send to embedding model (text-embedding-3-small)
            pgvector_docsearch = PGVector(
                collection_name= "my collection",
                connection_string=POSTGRES_DATABASE_URI,
                embedding_function=embeddings,
            )
            
            # Top 3k based on the embedding created from input_text
            searched_docs = pgvector_docsearch.similarity_search(prompt, k=3)
            
            
            if not searched_docs:
                """
                NO RELEVANT DOCUMENTS FOUND: If happens then something must have gone wrong with the embeddings
                """
                
                # final_response += "No relevant documents found.\n"
                # final_response += f"=> Sending request to OpenAI with input:\n{prompt}\n"
                # final_response += "============================================\n"
                
                # Sending prompt (query without context) to LLM
                response = self.llm([HumanMessage(content=prompt)])
                # Retrieve response content
                response_content = response.content if hasattr(response, 'content') else str(response)
                
                
                
                final_response += response_content
                return final_response
            
            
            """
            RELEVANT DOCUMENTS FOUND: Always
            """
            # yield "Relevant documents found.\n"
            
            # Only get one chunk (docs) for context to save cost

            result = ""
            for i in searched_docs:
                result += i.page_content + "\n"
            
            # Append user's query to context
            query = prompt + f"\n\nRelevant context:\n{result}\n"
            
            # yield f"=> Sending request to OpenAI with input:\n{query}\n"
            # yield "============================================\n"
            
            # Sending prompt (query with context) to LLM
            response = self.llm([HumanMessage(content=query)])
            # Retrieve response content
            response_content = response.content if hasattr(response, 'content') else str(response)
            
            # yield "\nRESULT:\n" 
            # yield response_content
            final_response += response_content
            return final_response
        except Exception as e:
            logging.error(f"Error in stream method: {e}. Sauce: app/chat/chat.py")
            return f"Error: {e}"


