from django.contrib import admin

from . import models

admin.site.register(models.Region)
admin.site.register(models.Country)
admin.site.register(models.User)
