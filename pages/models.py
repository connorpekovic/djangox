import uuid
from django.contrib.auth import get_user_model # new
from django.db import models
from django.urls import reverse

#Person
class Person(models.Model):
    id = models.UUIDField( # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('demo', args=[str(self.id)])

#Pet
class Pet(models.Model): # new
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

#Jobs
class Job(models.Model):
    id = models.UUIDField( # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    satisfaction= models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('demo', args=[str(self.id)])

#Hobby
class Hobby(models.Model):
    id = models.UUIDField( # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('demo', args=[str(self.id)])