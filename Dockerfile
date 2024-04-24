FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install nltk && \
    python -m nltk.downloader stopwords
CMD [ "python", "codescript.py" ]

