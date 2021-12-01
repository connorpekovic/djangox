import uuid 
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse
from accounts.models import CustomUser
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
# A Response simply object represents a response all 5 questions.
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
        ('Physiological', 'Physiological needs like food, water, sleep, shelter.'),
        ('Safety', 'Security of body, employment, resources, health.'),
        ('Education conditional', 'You are allowed unlimited education if you are qualified.'),
        ('Education unconditional', 'Unlimited free education.'),
    )

    PRYAMIDS = (
        ('Humans', 'Humans using ancient building techquins and hard work.'),
        ('Alien Intervention', 'Humans with alien intervention.'),
        ('Divine Intervention', 'Humans with divine intervention.'),

    )

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

    
    # def Q1_yes():
    #     q1_yesses = Response.objects.filter(Question1 = 'Yes').count()
    #     return 'test success'

    def total_Question1_no():
        pass

    def total_Questoin2_maybe():
        pass

    def total_Question_idk():
        pass
    
