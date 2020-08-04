# django-rest-react

[Django REST with React.js](https://www.valentinog.com/blog/drf/) as taught by Valentino Gagliardi

## TODO:

- [ ] README
  - [x] Django Setup
    - [x] Steps
    - [x] File tree
    - [ ] Review
  - [ ] React Setup
    - [ ] Steps
    - [ ] File Tree
    - [ ] Review
  - [ ] Add Starter instructions
    - [ ] Clone
    - [ ] Install Requirements
    - [ ] start Django Server
    - [ ] start React Server
- [ ] Starter
  - [x] Django Setup
  - [x] Django REST Setup
  - [ ] App creation - backend
    - [x] Model creation
    - [x] Model Migration
    - [x] Views creation
    - [x] Urls setup in project folder
    - [x] Urls setup in app folder
    - [x] Adjustment in settings.py for backend app
    - [ ] Test server for issues
  - [ ] App creation - frontend
    - [x] Views creation
    - [x] Urls setup in project folder
    - [x] Urls setup in app folder
    - [x] Adjustment in settings.py for frontend app
    - [ ] Component creation
    - [ ] Test server for issues

### Step-by-step:

#### Django settup:

1. [Setup Python environment](https://docs.python.org/3/library/venv.html) on your project folder (create and activate it).
2. Install [Django](https://www.djangoproject.com/download/) and [Django REST](https://www.django-rest-framework.org/).
3. Start the django project

```
django-admin startproject my_project
```

4. Create a django app from inside your project folder

```
cd my_project
django-admin startapp my_app
```

5. Go to `settings.py` and add the app and rest_framework to the INTALLED_APPS array

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',
    'rest_framework',
]
```

6. Create a [Django Model and run the migrations](https://www.digitalocean.com/community/tutorials/how-to-create-django-models)
7. Create the serializers

```python
from rest_framework import serializers
from .models import myModel

class MySerializer(serializers.ModelSerializer):
    class Meta:
    model = myModel
    fields = ('id', 'name', 'email')
```

8. Setup the [views](https://docs.djangoproject.com/en/3.0/topics/http/views/)
9. Setup the [urls](https://docs.djangoproject.com/en/3.0/ref/urls/)
10. Add a urls.py to the myapp directory (still need to finish description)

When this step is completed, the tree will look like this:

```
├── db.sqlite3
├── django_react
|  ├── asgi.py
|  ├── settings.py
|  ├── urls.py
|  ├── wsgi.py
|  ├── __init__.py
|  └── __pycache__
├── manage.py
└── myapp
   ├── admin.py
   ├── apps.py
   ├── migrations
   ├── models.py
   ├── serializers.py
   ├── tests.py
   ├── urls.py
   ├── views.py
   ├── __init__.py
   └── __pycache__
```

#### React Setup

1. From the project folder, create a frontend app:

```
django-admin startapp frontend
```

2.
