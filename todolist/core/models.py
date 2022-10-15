from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # MALE = "m"
    # FEMALE = "f"
    # SEX = [(MALE, "Male"), (FEMALE, "Female")]
    # sex = models.CharField(max_length=1, choices=SEX)

    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=40)
    # username = models.SlugField(max_length=20)
    pass