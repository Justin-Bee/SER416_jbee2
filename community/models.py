from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username


class Classes(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    date = models.DateField()
    models.IntegerField()


class Events(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateField()
    size = models.IntegerField()

class Equipment(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()

