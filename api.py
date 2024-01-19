from fastapi import FastAPI, UploadFile, File
import pdfplumber
from talk_to_your_reports import generate_answer
from vector_store_creator import vector_store_builder

app = FastAPI()

@app.post("/talk-to-your-report/upload-report")
async def upload_pdf(file: UploadFile = File(...)):
    # document = await file.read()
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=1)
    
    text = text.replace("\n", " ")
    vector_store_builder(text)

@app.post("/talk-to-your-report/query")  
def process_query(query: str):
    answer = generate_answer(query)
    return {"answer": answer}

@app.get("/talk-to-your-report/health-check")
def health_check():
    return {"status": "ok"}