from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
