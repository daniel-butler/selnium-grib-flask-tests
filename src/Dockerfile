FROM python:3.8-buster

COPY ./requirements.txt /tmp/

RUN pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY ./src /src

WORKDIR /src
