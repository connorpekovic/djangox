from django.contrib import admin
from .models import Response

# Description: Register your models here. If you want the model to appear in 
# the admin screens, you must include it here with these 2 lines of code.
#
# Improvements: Add inline detail.

class ResponceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Response, ResponceAdmin)