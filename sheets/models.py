from django.db import models

# Create your models here.

class Sheet(models.Model):
    name = models.CharField(max_length=100)
    sheetjson = models.TextField(default="")
