from rest_framework import serializers
from .models import myapp


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = myapp
        fields = ('id', 'name', 'email')
