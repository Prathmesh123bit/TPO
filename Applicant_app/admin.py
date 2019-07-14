from django.contrib import admin
from Applicant_app import models
# Register your models here.
admin.site.register(models.Branche)
admin.site.register(models.AcademicYear)
admin.site.register(models.Semester)
admin.site.register(models.Student)
