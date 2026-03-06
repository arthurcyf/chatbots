from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4

from dotenv import load_dotenv
load_dotenv()

# config
DATA_PATH = r"./data"
CHROMA_PATH = r"./chroma_db"

# intiiate the embeddings model
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

# initiate the vector store
vector_store = Chroma(
    collection_name="example_collection", 
    embedding_function=embedding_model, 
    persist_directory=CHROMA_PATH
    )

# loading the documents
loader = PyPDFDirectoryLoader(DATA_PATH)

raw_documents = loader.load()

# splitting the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, 
    chunk_overlap=200, 
    length_function=len, 
    is_separator_regex = False
    # keep_separator = True # if you want to keep the separator in the chunks, you can set this to True
    # strip_whitespace = True # if you want to strip whitespace from the chunks, you can set this to True
    # add_start_index = True # if you want to add the start index of the chunk in the original document, you can set this to True
)

# create the chunks
chunks = text_splitter.split_documents(raw_documents)

# create the unique ids for the chunks
uuid = [str(uuid4()) for _ in range(len(chunks))]

# add the chunks to the vector store
vector_store.add_documents(documents = chunks, ids=uuid) # adds the chunks and the ids to the vector db