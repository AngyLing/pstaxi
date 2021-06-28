from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=210, default='', blank=True)
