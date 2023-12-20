from django.db import models

# Create your models here.
# yourapp/models.py

from django.contrib.auth.models import User
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'


# models.py

from django.db import models

class CreateNewUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

