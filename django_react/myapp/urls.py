from django.urls import path
from . import views

urlpatterns = [
    # this is a more specific url path for the API!
    path('api/myapp/', views.myListCreate.as_view())
]
