FROM python:3.8-alpine
MAINTAINER Meet Patel

## helps with making python run correctly in docker
ENV PYTHONUNBUFFERED 1

## copies requirements file from directory adjacent to docker file to a file inside docker image
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

## creates folder on docker image
RUN mkdir /app
## docker image defaults to that folder
WORKDIR /app
## copies from local app to docker image app folder
COPY ./app /app

RUN adduser -D user
USER user