FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update; apt-get install -y --no-install-recommends git libpq-dev build-essential nano; rm /var/lib/apt/lists/*

COPY ./ /app

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "analysis/ethereum_lstm.py"]
