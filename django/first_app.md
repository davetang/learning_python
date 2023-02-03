## Setup

Install Django using a [virtual
environment](https://docs.python.org/3/library/venv.html). I will create a
virtual environment in this directory.

```bash
python3 -m venv .
source ./bin/activate

which pip
# ~/github/learning_python/django/bin/pip

pip install --upgrade pip

which python
# ~/github/learning_python/django/bin/python

python --version
# Python 3.8.3
```

Now to install.

```bash
python -m pip install Django
python -m django --version
# 4.1.6
```

## Writing your first Django app, part 1

[Creation of a basic poll
application](https://docs.djangoproject.com/en/4.1/intro/tutorial01/) that
consists of two parts:

1. A public site for viewing and voting in polls
2. An admin site for modifying polls

Auto-generate some code that establishes a Django
[project](https://docs.djangoproject.com/en/4.1/glossary/#term-project), which
is a Python package that contains all the settings for an instance of Django.
This includes database configs, Django-specific options, and
application-specific settings.

```bash
django-admin startproject polling_site

tree --charset ascii polling_site/
polling_site/
|-- manage.py
`-- polling_site
    |-- asgi.py
    |-- __init__.py
    |-- settings.py
    |-- urls.py
    `-- wsgi.py

1 directory, 6 files
```

* The root `polling_site` directory is a container for your project.
* `manage.py` is a command-line utility that lets you interact with this Django
project in various ways.
* The inner `polling_site` directory is the actual Python package for your
project. Its name is the Python package name you’ll need to use to import
anything inside it (e.g. mysite.urls).
* `__init__.py` is an empty file that tells Python that this directory should
be considered a Python package.
* `settings.py` contains the settings/configuration for this Django project.
* `urls.py` contains the URL declarations for this Django project; a “table of
contents” of your Django-powered site.
* `asgi.py` is an entry-point for ASGI-compatible web servers to serve your project.
* `wsgi.py` is an entry-point for WSGI-compatible web servers to serve your project.

Verify that the Django project works by starting the Django development server,
a lightweight web server written purely in Python. This is used to quickly
develop projects without having to configure a production server such as
Apache.

```bash
cd polling_site
./manage.py runserver 8001

# Watching for file changes with StatReloader
# Performing system checks...
# 
# System check identified no issues (0 silenced).
# 
# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.
# February 03, 2023 - 00:42:38
# Django version 4.1.6, using settings 'polling_site.settings'
# Starting development server at http://127.0.0.1:8001/
# Quit the server with CONTROL-C.
```

Each application in Django consists of a Python package that follows a certain
convention. Django comes with a utility that automatically generates the basic
directory structure of an app. The apps can be created anywhere on the Python
path. In this example, the poll app will be created in root `polling_site`
directory so that it can be imported as its own top-level module, rather than a
submodule of `polling_site`.

```bash
./manage.py startapp polls

tree --charset ascii polls
# polls
# |-- admin.py
# |-- apps.py
# |-- __init__.py
# |-- migrations
# |   `-- __init__.py
# |-- models.py
# |-- tests.py
# `-- views.py
# 
# 1 directory, 7 files
```

To write the first view, paste the following code in `polls/views.py`; this is
the simplest view possible in Django.

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

To call the view, we need to map it to a URL and to do this, we need a URLconf.
To create a URLconf in the polls directory, create a file called
`polls/urls.py` and include the following code.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

The next step is to point the root URLconf at the `polls.urls` module. Add an
import for `django.urls.include` and insert an `include()` in the `urlpatterns`
list to `polling_site/urls.py`.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

The `include()` function allows referencing other URLconfs. Whenever Django
encounters `include()`, it chops off whatever part of the URL matched up to
that point and sends the remaining string to the included URLconf for further
processing.

The `path()` function is passed four arguments, two required: `route` and
`view`, and two optional `kwargs`, and `name`. `route` is a string that
contains a URL pattern. When Django finds a matching pattern, it calls the
specified view function with an `HttpRequest` object as the first argument and
any "captured" values from the route as keyword arguments.

Check whether everything is working at `localhost:8001/polls`.

```bash
./manage.py runserver 8001
```
