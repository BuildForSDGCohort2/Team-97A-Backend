from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Package)
admin.site.register(models.Tracker)
admin.site.register(models.Wallet)
admin.site.register(models.Transaction)
