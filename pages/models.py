import uuid 
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse
from accounts.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Starlog:  Relating objects need to be mentioned parent-first.
        
# Create your models here.
# This represents a users responce to a Question object.
# Assumption: Perception of truth change throughout time.
class Response(models.Model):

    FATE = (
        ('Yes', 'Yes. I believe in determination'),
        ('No', 'No. I believe in self-determination.'),
        ('Maybe', 'I cant tell if there is fate, but maybe there is luck.'),
        ('Idk', 'I do not know.'),
    )

    MEANING = (
        ('Yes', 'Yes. My life had a meaning. I am here with a purpose.'),
        ('No', 'No. Life is random and lacks meaning.'),
    )

    GOAL = (
        ('Please God', 'Appease God\'s will.'),
        ('Panspermia', 'Spread life into the universe (a.k.a. panspermia).'),
        ('Persist', 'Preserve life on earth.'),
        ('Idealism', 'Uphold right and wrong.'),
    )

    RIGHTS = (

        ('Water', 'Water is a human right.'),
        ('Water, Food', 'Water and food are human rights.'),
        ('Water, Food, and Housing', 'Water, food, and housing are human rights.'),
        # ('Justice','Everyone deserves blind justice.'),
        ('None', 'Nothing is guaranteed in life by others.'),

    )

    GLOBALIZATION = (
        ('Yes', 'Yes. Globalization brought billions out of poverty.'),
        ('No', 'No. Globalization created unsatiable demand and displaced western manfactuering jobs.'),
    )

    PRYAMIDS = (
        ('Humans', 'Humans using ancient building techquins and hard work.'),
        ('Alien Intervention', 'Humans with alien intervention.'),
        ('Divine Intervention', 'Humans with divine intervention.'),

    )


    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False)
    created_by = models.OneToOneField(
        CustomUser,
        on_delete = models.CASCADE)
    Question1 = models.TextField(choices=FATE)
    Question2 = models.TextField(choices=MEANING)
    Question3 = models.TextField(choices=GOAL)
    Question4 = models.TextField(choices=RIGHTS)
    Question5 = models.TextField(choices=PRYAMIDS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_by)


#Django signal that generates a unique slug for an object. Very much like an event from .NET.
# @receiver(pre_save, sender=Response)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)