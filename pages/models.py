import uuid 
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

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

    CLIMATE_RESPONCE = (
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

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    Stregthen_social_safety_nets = models.TextField(choices=SOCIAL_SAFETY_NET)
    Nationalize_healthcare = models.TextField(choices=NATIONALIZE_HEALTHCARE)
    Climate_responce = models.TextField(choices=CLIMATE_RESPONCE)
    Should_we_limit_urban_sprall = models.TextField(choices=URBAN_SPRALL)
    Do_you_support_or_oppose_globalization = models.TextField(choices=GLOBALIZATION)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_by)