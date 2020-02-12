FROM python:3.8-buster

COPY functional_tests/requirement-tests.txt /tmp/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY ./functional_tests /src

WORKDIR /src
