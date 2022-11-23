# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    endereco = models.CharField(max_length=35, null = True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True)

    def __str__(self):
        return self.endereco
