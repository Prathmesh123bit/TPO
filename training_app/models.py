from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Internship(models.Model):
    internshipId = models.AutoField(primary_key = True)
    internshipName = models.CharField(max_length = 100, help_text = "Internship Name")
    internshipDetails = models.CharField(max_length = 225, help_text = "Description")
    marks = models.IntegerField()

    def __str__(self):
        return self.internshipName

class Gd(models.Model):
    gdId = models.AutoField(primary_key = True)
    gdName = models.CharField(max_length = 100,help_text = "Group Discussion Topic")
    marks = models.IntegerField()

    def __str__(self):
        return self.gdName

class MockInterview(models.Model):
    mockinterviewid = models.AutoField(primary_key = True)
    mockinterviewName = models.CharField(max_length = 100, help_text = "Conducted By")
    marks = models.IntegerField()

    def __str__(self):
        return self.mockinterviewName

class Resume(models.Model):
    resumeId = models.AutoField(primary_key = True)
    marks = models.IntegerField()

    def __str__(self):
        return self.resumeId

class Aptitude(models.Model):
    aptitudeId = models.AutoField(primary_key = True)
    aptitudeName = models.CharField(max_length = 100, help_text = "Conducted By")
    marks = models.IntegerField()

    def __str__(self):
        return self.aptitudeId
