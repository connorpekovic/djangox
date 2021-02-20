from django.contrib import admin
from .models import Person, Pet, Hobby, Job

class PetInline(admin.TabularInline):
    model = Pet

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PetInline,
    ]
    list_display = ("title", "author", "price",)


class HobbyAdmin(admin.TabularInline):
    model = Hobby


admin.site.register(Person, PersonAdmin) 