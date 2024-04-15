from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.location_name


class User(models.Model):
    login = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=25, unique=True)
    user_password = models.CharField(max_length=25)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.login + " - " + self.email

class Advertisement(models.Model):
    title = models.CharField(max_length=70)
    ad_text = models.CharField(max_length=700)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)  # Додайте це поле для вказівки на публічність оголошення

    def __str__(self):
        return self.title