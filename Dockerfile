FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update; apt-get install -y git libpq-dev build-essential nano

COPY ./ /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "analysis/ethereum_lstm.py"]
