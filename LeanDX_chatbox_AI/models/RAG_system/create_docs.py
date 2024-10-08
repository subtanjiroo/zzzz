import os
import csv
from langchain_community.document_loaders import PyPDFLoader, CSVLoader,Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

#todo: install docx2txt

def create_docs_for_pdf(pdf_path: str):
    """
    Load and split the given pdf into chunks (docs)

    1. Extract text from the specified PDF.
    2. Divide the extracted text into manageable chunks (docs).

    :param document_id: The unique identifier for the PDF.
    :param pdf_path: The file path to the PDF.

    Example Usage:

    create_embeddings_for_pdf('123456', '/path/to/pdf')
    """

    # PDF loader
        #TODO: Try to find the best pdf loader for use case.
        #TODO: Handle file size of pdf.

    loader = PyPDFLoader(
        file_path = pdf_path,
        extract_images = True,
    )

    #Text Splitter
        #TODO: Try to find the best text splitter for use case.
        #TODO: Try to find the best chunk size and overlap for use case.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=20)

    documents = loader.load_and_split(text_splitter)

    return documents


# def create_docs_for_csv(csv_path: str, delimeter, fieldnames):
#     """
#     Load and split the given csv into chunks (docs)
#
#     1. Extract text from the specified CSV.
#     2. Divide the extracted text into manageable chunks (docs).
#
#     :param csv_path: The file path to the CSV.
#
#     Example Usage:
#
#     create_docs_for_csv('/path/to/csv')
#     """
#
#     # Check delimiter of csv file
#     with open(csv_path, 'r') as file:
#         # Create a Sniffer object
#         sniffer = csv.Sniffer()
#         # Read a small sample from the file
#         sample = file.read(1024)
#         # Detect the delimiter
#         detected_dialect = sniffer.sniff(sample)
#
#
#     delimiter = detected_dialect.delimiter
#
#     #TODO: Pop up to user to select the delimiter if not detected.
#
#
#
#     # Load the CSV and split it into rows
#     loader = CSVLoader(
#         file_path = csv_path,
#         csv_args={
#             'delimiter': delimiter,
#             'quotechar': '"',
#             'fieldnames': ['Index', 'Height', 'Weight']
#         }
#     )
#
#
#     # Split the rows into chunks
#
#     return docs
def create_docs_for_string(text: str):
    """
    Split the given text into chunks (docs)

    Divide the given text into manageable chunks (docs).

    :param text: The text to split into chunks (docs).

    Example Usage:

    create_docs_for_string('This is a sample text')
    """
    api_key = os.environ["OPENAI_API_KEY"]
    
    # Check if the API key is set
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    
    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=20)
    docs = text_splitter.split_text(text)
    return docs

def create_docs_for_xlss(docx_path):
    """
    Load and split the given docx into chunks (docs)

    1. Extract text from the specified DOCX.
    2. Divide the extracted text into manageable chunks (docs).

    :param docx_path: The file path to the DOCX.

    Example Usage:

    create_docs_for_xlss('/path/to/docx')
    """


