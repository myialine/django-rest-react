from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
