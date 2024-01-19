from langchain import PromptTemplate
from langchain.chains import RetrievalQA    
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import prompts
import llama_2_7b

def set_qa_prompt():
    prompt = PromptTemplate(template = prompts.qa_template,
                            input_variables=['context', 'question'])
    return prompt

def build_retrieval_qa(llm, prompt, vectordb):
    dbqa = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type= 'stuff',
                                       retriever = vectordb.as_retriever(search_kwargs = {'k':2}),
                                       return_source_documents = True,
                                       chain_type_kwargs={'prompt':prompt})
    return dbqa

def setup_query_answering():
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs = {'device': 'cpu'})
    vectordb = FAISS.load_local('vectorstore/db_faiss', embeddings)
    qa_prompt = set_qa_prompt()
    retrieval_qa = build_retrieval_qa(llama_2_7b.llm, qa_prompt, vectordb)
    
    return retrieval_qa