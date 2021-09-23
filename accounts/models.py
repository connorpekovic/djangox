import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.views.generic import edit 

# User ID needs to be UUID
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email