from django.db import models

# Create your models here.


class test(models.Model):
    pep = models.CharField( max_length=50)