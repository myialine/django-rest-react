from django.urls import path
from . import views

# this is the url pattern for the react_frontend.
urlpatterns = [
    path('', views.index),
]
