from .models import Person
from .serializers import MySerializer
from rest_framework import generics


# Create your views here.

'''Generic API Views - a view for listing and creating models
ListCreateAPIView https://www.django-rest-framework.org/api-guide/generic-views/ '''


class myListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = MySerializer
