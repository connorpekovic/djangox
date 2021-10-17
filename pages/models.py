import uuid 
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Starlog:  Relating objects need to be mentioned parent-first.
        
# Create your models here.
# This represents a users responce to a Question object.
# Assumption: Perception of truth change throughout time.
class Response(models.Model):

    SOCIAL_SAFETY_NET = (
        ('Yes', 'Yes. Enact UBI (Universal Basic Income).'),
        ('Same', 'No. Spending levels as is'),
        ('Reduce', 'Negatory. Slowly stop funding Social Security'),
    )

    NATIONALIZE_HEALTHCARE = (
        ('Yes', 'Yes. Nationalize it like the NHS in England.'),
        ('No', 'No. Leave it as is.'),
    )

    CLIMATE_RESPONSE = (
        ('Strong', 'Take extraordinary measures. Enact enforceable laws.'),
        ('Senseable', 'Take oridnary meaures, don\'t tread on my consumption.'),
        ('Capitalist', 'Take no meaures.'),
    )

    URBAN_SPRALL = (
        ('Yes', 'Yes. Promote city living.'),
        ('No', 'No. Don\'t tread on me.'),
    )

    GLOBALIZATION = (
        ('Yes', 'Yes. Globalization increases the quality of life and brings rich cultures together.'),
        ('No', 'No. We need to focus on issued at home. Things will work out better in the end.'),
    )

    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False)
    created_by = models.OneToOneField(
        CustomUser,
        on_delete = models.CASCADE)
    Question1 = models.TextField(choices=SOCIAL_SAFETY_NET)
    Question2 = models.TextField(choices=NATIONALIZE_HEALTHCARE)
    Question3 = models.TextField(choices=CLIMATE_RESPONSE)
    Question4 = models.TextField(choices=URBAN_SPRALL)
    Question5 = models.TextField(choices=GLOBALIZATION)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_by)


#Django signal that generates a unique slug for an object. Very much like an event from .NET.
# @receiver(pre_save, sender=Response)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)