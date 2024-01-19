from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
	
# Load PDF file from data path
def vector_store_builder(document):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=50)
    texts = text_splitter(document)

    # Load embeddings model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    # Build and persist FAISS vector store
    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local('vectorstore/db_faiss')