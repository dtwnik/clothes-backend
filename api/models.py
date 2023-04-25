from django.db import models

# Create your models here.
SEASONS = [
    ("Multi", "Multi"),
    ("Spring", "Весна"),
    ("Summer", "Лето"),
    ("Autumn", "Осень"),
    ("Winter", "Зима"),
]
class Men(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='img', blank=True)
    type = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    composition = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=255, choices=SEASONS, default='Multi')

    def __str__(self):
        return self.title


class Woman(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='img', blank=True)
    type = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    composition = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=255, choices=SEASONS, default='Multi')

    def __str__(self):
        return self.title


class Kids(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='img', blank=True)
    type = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    composition = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=255, choices=SEASONS, default='Multi')

    def __str__(self):
        return self.title


class Bestseller(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='img', blank=True)
    type = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    composition = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=255, choices=SEASONS, default='Multi')

    def __str__(self):
        return self.title
