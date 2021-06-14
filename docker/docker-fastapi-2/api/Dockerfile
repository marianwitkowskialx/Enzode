FROM python:3.9-slim

RUN apt-get update && apt-get install -y netcat

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt


