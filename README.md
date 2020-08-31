# demo-cas-server

A demo CAS server work with [django-cas-ng/example](https://github.com/django-cas-ng/example) to show how to integrate with [django-cas-ng](https://djangocas.dev) and [python-cas](https://github.com/python-cas/python-cas).

- [Step by step to setup a django-cas-ng example project](https://djangocas.dev/blog/django-cas-ng-example-project/)
- [python-cas Flask example](https://djangocas.dev/blog/python-cas-flask-example/)

Demo server URL: https://django-cas-ng-demo-server.herokuapp.com/

Python 3 and Django 2.2 are required.

```
pip install -r requirements.txt
python manage.py runserver
```

## Using docker

```bash
docker-compose up -d
```

## Test

Open `http://127.0.0.1:8000/cas/login`

---
[**NOTE**]:
 
Before run server, create db and a superuser:

 - `python manage.py migrate`
 - `python manage.py createsuperuser` 
 
In docker mode:

 - `docker exec -it cas-server python manage.py migrate`
 - `docker exec -it cas-server python manage.py createsuperuser`
