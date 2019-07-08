from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    companyId=models.AutoField(primary_key=True)
    CN=(
        ('TCS','TCS'),
        ('Infosycs','Infosycs'),
        ('Wipro','Wipro'),
        ('Percistence','Percistence'),
        ('Godrej','Godrej'),
        ('IFB','IFB'),
        ('LNT','LNT'),
        ('Siemens','Siemens'),

    )
    companyName=models.CharField(max_length=100,choices=CN,help_text="Company Name")

    def __str__(self):
        return self.companyName
class AcademicYear(models.Model):
    yearId=models.AutoField(primary_key=True)
    yearName=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.yearId
class Semester(models.Model):
    semesterid=models.AutoField(primary_key=True)
    semesterName=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.semesterName
