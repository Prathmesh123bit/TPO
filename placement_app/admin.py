from django.contrib import admin
from placement_app import models
# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.AcademicYear)
admin.site.register(models.Semester)
