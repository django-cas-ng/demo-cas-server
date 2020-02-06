from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    body = """<!DOCTYPE html>
<html>
  <head>
    <title>django-cas-ng and python-cas CAS demo server</title>
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
  </head>
  <body>
    <h1>Welcome to django-cas-ng and python-cas CAS demo server</h1>
    <p>Related posts:</p>
    <ul>
        <li><a href="https://djangocas.dev/blog/django-cas-ng-example-project/">Step by step to setup a django-cas-ng example project</a></li>
        <li><a href="https://djangocas.dev/blog/python-cas-flask-example/">python-cas Flask example</a></li>
    </ul>
    <hr>
    <p><a href="https://djangocas.dev/">Project homepage</a></p>
  </body>
</html>
        """
    return HttpResponse(body)


def ping(request: HttpRequest) -> HttpResponse:
    return HttpResponse('pong', content_type="text/plain")
