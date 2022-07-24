FROM python:latest

COPY . /opt
WORKDIR /opt
RUN apt-get update -y
RUN pip install -r requirements.txt