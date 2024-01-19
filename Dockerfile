FROM python:3.10
WORKDIR /app
COPY ./api.py /app/
COPY ./llama_2_7b.py /app/
COPY ./prompts.py /app/
COPY ./retrieval_qa.py /app/
COPY ./talk_to_your_reports.py /app/
COPY ./vector_store_creator.py /app/
COPY ./llama-2-7b-chat.ggmlv3.q8_0.bin /app/
COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8090"]