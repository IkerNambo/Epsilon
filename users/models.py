from django.db import models
from django.contrib.auth.models import AbstractBaseUser,  AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.




    # for user auth
    #User = models.OneToOneField(User, on_delete=models.CASCADE, null=True)