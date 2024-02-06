FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

# update the base OS packages
RUN apk update \
  && apk upgrade \
  && apk add --no-cache bash \
  && apk add --no-cache --update sqlite

RUN mkdir /app
WORKDIR /

ADD requirements.txt /app
RUN pip install -r app/requirements.txt

# install the python requirements
RUN pip install --no-cache-dir -U pip pip-tools \
  && pip-sync --pip-args "--no-cache-dir" app/requirements.txt

ADD . /app

WORKDIR /app
RUN python manage.py makemigrations hkey
RUN python manage.py migrate
# Load fixture data
RUN python manage.py loaddata fixtures/auth_group.json
RUN python manage.py loaddata fixtures/hkey_grouper.json
RUN python manage.py loaddata fixtures/hkey_huser.json
RUN python manage.py loaddata fixtures/hkey_memberof.json
# RUN demo_data/import.sh

# HTTP version
EXPOSE 9001
CMD python manage.py runserver 0.0.0.0:9000

# HTTPS version
# EXPOSE 9001
# CMD python manage.py runsslserver 0.0.0.0:9001
