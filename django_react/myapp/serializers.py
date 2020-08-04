from rest_framework import serializers
from .models import Person


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'email')
