FROM python:3.12-slim

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader vader_lexicon

COPY . .

CMD ["uvicorn", "app.main:app"]