from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here
    fullname = models.CharField(max_length=40)

    def __str__(self):
        return self.email