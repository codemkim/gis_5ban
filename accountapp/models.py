from django.db import models

# Create your models here.


class HelloWorld(models.Model):
    text = models.CharField(null=False, max_length=255)
