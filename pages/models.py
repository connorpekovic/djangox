import uuid 
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse
from accounts.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
# A Response to the question of "Who built the pryamids?"
class Response(models.Model):


    CHOICE_LIST = (
        ('not legitimate', 'These incidents are not legitimate. Perhaps it is a money grab by a bad faith defence agency.'),
        ('legitimate earthly', 'All UFOs must have earthly origin. The vastness of space is too grand for extraterrestrial life to make it. Perhaps they are from another state or non-state actor.'),
        ('legitimate earthly few extraterrestrial', 'Some UFOs have earthly origins, but accounts like Bob Lazar could possibly mean extraterrestrial origins.'),
        ('legitimate extraterrestrial', 'Bob Lazar and Captian David Fravor are not lying and extraterrestrial space crafts come into contact with earth.'),
    )

    created_by = models.OneToOneField(
        CustomUser,
        on_delete = models.CASCADE)
    Question1 = models.TextField(choices=CHOICE_LIST)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_by)

