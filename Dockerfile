FROM python:3.13.1-alpine
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY main.py /app
COPY features /app/features
COPY api /app/api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]