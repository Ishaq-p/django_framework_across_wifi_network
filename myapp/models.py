from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


# class File(models.Model):
#     name = models.CharField(max_length=255)
#     file = models.FileField(upload_to='uploads/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
