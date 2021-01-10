from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Client)
admin.site.register(models.Vendor)
admin.site.register(models.SubVendor)
admin.site.register(models.Team)
admin.site.register(models.Employee)
admin.site.register(models.Attendance)
