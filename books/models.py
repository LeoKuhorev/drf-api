from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BookRecord(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, blank=True)
    date_given_out = models.DateTimeField(null=True, blank=True)
    date_returned = models.DateTimeField(null=True, blank=True)
    record_created_at = models.DateTimeField(auto_now=True)
    record_created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
