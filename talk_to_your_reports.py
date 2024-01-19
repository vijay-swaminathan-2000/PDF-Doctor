import retrieval_qa
def generate_answer(query):
    dbqa = retrieval_qa.setup_query_answering()
    response = dbqa({'query': query})
    return response["result"]