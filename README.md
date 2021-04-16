# hkey-demo-cas-server

A demo CAS server work with [django-cas-ng/example](https://github.com/django-cas-ng/example) to show how to integrate with [django-cas-ng](https://djangocas.dev) and [python-cas](https://github.com/python-cas/python-cas).

## Local development setup

```
pip install -r requirements-dev.txt
pre-commit install
```

## Run locally using docker

```bash
docker-compose up
```

## Run locally the old way

```
python manage.py migrate
./demo_data/import.sh
python manage.py runserver 9000
```

## Default user/passwd combos

| username | password |
| -------- | -------- |
| admin    | testinstructor |
| dr_fauci | testinstructor
| producer |  |
| nancy    |  |
| joe      | teststudent |

(dr_fauci has 2 courses)

## Test

Open `http://127.0.0.1:9000/cas/login`

---
