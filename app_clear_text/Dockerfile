FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app_clear_text/ .
COPY comman_utils/ ./comman_utils

CMD ["python", "main.py"]
