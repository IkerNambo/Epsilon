from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class SiteUsers(models.Model):
    UserName = models.CharField(max_length=50, blank=False)
    EmailAddress = models.EmailField(max_length=250, blank=False, null=False, unique=True)
    Password = models.CharField(max_length=250, blank=False)
    Staff = models.BooleanField(blank=True, null=False, default=False)