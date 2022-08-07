import uuid

from django.db import models

from .constants import CATEGORIES, FILETYPES, LANGUAGES, YES_OR_NO


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=3000)
    language = models.CharField(max_length=5, choices=LANGUAGES)
    link = models.URLField()
    copyright = models.CharField(max_length=128)

    # Itunes Specific Fields
    image = models.ImageField()
    category = models.CharField(max_length=40, choices=CATEGORIES)
    explicit = models.BooleanField()
    author = models.CharField(max_length=120)
    owner_name = models.CharField(max_length=120)
    owner_email = models.EmailField()
    block = models.CharField(max_length=3, choices=YES_OR_NO)
    complete = models.CharField(max_length=3, choices=YES_OR_NO)


class Episode(models.Model):
    title = models.CharField(max_length=128)
    file = models.FileField()
    file_type = models.CharField(max_length=20, choices=FILETYPES)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    published_date = models.DateTimeField()
    description = models.TextField(max_length=3000)
    link = models.URLField()

    # Itunes Specific Fields
    duration = models.IntegerField()
    image = models.ImageField()
