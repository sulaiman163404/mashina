from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username
