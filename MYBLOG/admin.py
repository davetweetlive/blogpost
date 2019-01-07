from django.contrib import admin
from . import models

# Register your models her
admin.site.register(models.Profile)
admin.site.register(models.Post)
admin.site.register(models.Comment)
