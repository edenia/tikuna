FROM python:3.8-slim-buster

RUN apt-get update; apt-get install -y --no-install-recommends \
    git libpq-dev build-essential nano procps curl iputils-ping; \
    rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash tikuna
USER tikuna
WORKDIR /home/tikuna/app
COPY ./ /home/tikuna/app

ENV PATH="${PATH}:/home/tikuna/.local/bin"
RUN pip3 install --no-warn-script-location --no-cache-dir --upgrade pip
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt
USER root
RUN chown -R tikuna:tikuna /home/tikuna/app
USER tikuna

CMD ["python", "app.py"]
