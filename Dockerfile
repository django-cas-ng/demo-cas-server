FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /

ADD requirements.txt /app
RUN pip install -r app/requirements.txt
ADD . /app

WORKDIR /app
CMD python manage.py runserver 0.0.0.0:8000
