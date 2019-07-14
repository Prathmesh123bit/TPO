from django.db import models
from django.contrib.auth.models import User


class AcademicYear(models.Model):
    yearId=models.AutoField(primary_key=True)
    yearName=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.yearName


class Semester(models.Model):
    semesterid=models.AutoField(primary_key=True)
    semesterName=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.semesterName


class Branche(models.Model):
    branchId=models.AutoField(primary_key=True)
    BN=(
        ('computer','computer'),
        ('Mech','Mech'),
        ('civil','civil'),
        ('ETC','Etc'),

    )
    branchName=models.CharField(max_length=100,choices=BN,help_text="Branch Name")
    def __str__(self):
        return self.branchName


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollNo = models.IntegerField(primary_key=True)
    percent=models.IntegerField(null = True, help_text = "Percentage")
    year = models.ForeignKey(AcademicYear, related_name="AcademicYearId",null=False,on_delete=models.CASCADE)
    semesterId=models.ForeignKey(Semester, related_name="StudentSemesterId",null=False,on_delete=models.CASCADE)
    branchId=models.ForeignKey(Branche, related_name="StudentBranchId",null=False,on_delete=models.CASCADE)
    SEX= (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        )
    gender =models.CharField(max_length=10, choices = SEX, null = True, help_text = "Gender")

    def __str__(self):
        return format(self.user.username)

    class Meta:
        ordering = ["-user"]
        permissions = (("is_student", "is_student"),)

    def get_absolute_url(self):
        return reverse('profile')
