# hkey-demo-cas-server

A demo CAS server work with [django-cas-ng/example](https://github.com/django-cas-ng/example) to show how to integrate with [django-cas-ng](https://djangocas.dev) and [python-cas](https://github.com/python-cas/python-cas).

## Local development setup

```
pip install -r requirements-dev.txt
pre-commit install
```

## Run locally using docker

```bash
docker build -t demo-cas-server .
docker-compose up
```

## Run locally 

```
python manage.py migrate
./demo_data/import.sh
# HTTP
python manage.py runserver 9000

# HTTPS
python manage.py runsslserver 127.0.0.1:9001 &
```

## Default user/passwd combos

| username | password |
| -------- | -------- |
| admin    | rivendel |
| dr_fauci | testinstructor
| producer |  |
| nancy    |  |
| joe      | teststudent |
| dokiadmin| okaydoki   |
| dokistaff| okaydoki   |
| dokiuser | okaydoki   |

(dr_fauci has 2 courses)



## Test

Open `http://127.0.0.1:9000/cas/login`

or

Open `https://127.0.0.1:9001/cas/login`

## To use the https service as a demo cas server (in porta or doki)

Add these settings to .env or to <project>/settings.py

    # Point to the service using https
    CAS_SERVER_URL=https://localhost:9001/cas/

    # Turn off ssl VERIFICATION to use self signed certs
    CAS_VERIFY_SSL_CERTIFICATE=False

