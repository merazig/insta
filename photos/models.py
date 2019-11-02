from django.core.files.storage import FileSystemStorage
from django.db import models


class Insta(models.Model):
    photo = models.ImageField(upload_to='insta/')