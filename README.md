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
  - [x] App creation - backend
    - [x] Model creation
    - [x] Model Migration
    - [x] Views creation
    - [x] Urls setup in project folder
    - [x] Urls setup in app folder
    - [x] Adjustment in settings.py for backend app
    - [x] Test server for issues
  - [x] App creation - frontend
    - [x] Views creation
    - [x] Urls setup in project folder
    - [x] Urls setup in app folder
    - [x] Adjustment in settings.py for frontend app
    - [ ] Component creation (optional)
    - [x] Test server for issues

### Clone starter:

### Making the starter Step-by-step:

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

2. Create the `src`, `static`, and `templates` folders. Inside `static` and `templates`, create a `frontend` folder.
   The diretory structure for this project should look something like this:

```
C:\Users\brali\source\repos\django-react\django_react\frontend
├── migrations
|  └── __pycache__
├── src
|  └── components
├── static
|  └── frontend
├── templates
|  └── frontend
└── __pycache__
```

3. Setup [React](https://reactjs.org/), [webpack](https://webpack.js.org/) and [babel](https://babeljs.io/):
   On the frontend folder, using the terminal:

```
cd ./frontend
npm init -y
```

Then install webpack:

```
npm i webpack webpack-cli --save-dev
```

Configure scripts for webpack on `package.json`:

```json
"scripts":{
  "dev": "webpack --mode development ./src/index.js --output ./static/frontend/main.js",
  "build": "webpack --mode production ./src/index.js --output ./static/frontend/main.js",
}
```

Then install babel:

```
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
```

Now install React:

```
npm i react react-dom --save-dev
```

Create a `.babelrc` file inside `./frontend`:

```json
{
	"presets": ["@babel/preset-env", "@babel/preset-react"]
}
```

And then create a `webpack.config.js` with the following:

```javascript
module.exports = {
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader",
				},
			},
		],
	},
};
```

4. Prepare the frontend
   On `./frontend/views.py`:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')
```

On `./frontend/templates/frontend/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Django REST with React</title>
</head>
<body>
<div id="app">
    <!-- React will load here -->
</div>
</body>
{% load static %}
<script src="{% static "frontend/main.js" %}"></script>
</html>
```
