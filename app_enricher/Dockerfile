FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app_enricher/ .
COPY comman_utils/ ./comman_utils

CMD ["python", "manager_the_enricher.py"]
