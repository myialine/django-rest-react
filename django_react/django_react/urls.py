from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # this is a generic url mapping. A more specific one is inside ./myapp
    path('', include('myapp.urls')),

    # this is the react specific url config! It also has its own urls.py:
    path('', include('react_frontend.urls')),
]
