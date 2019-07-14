from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Designation(models.Model):
    designationId = models.AutoField(primary_key=True)
    JN = (
                ('Trainee Engineer','Trainee Engineer'),
                ('Software Engineer','Software Engineer'),
                ('System Analyst','System Analyst'),
                ('Programmer Analyst','Programmer Analyst'),
                ('Senior Software Engineer','Senior Software Engineer'),
                ('Project Lead','Project Lead'),
                ('Project Manager','Project Manager'),
                ('Program Manager','Program Manager'),
                ('Architect','Architect'),
                ('Technical Specialist','Technical Specialist'),
                ('Deliver Manager','Deliver Manager'),
                ('Delivery Head','Delivery Head'),
                ('Business Analyst','Business Analyst'),
                ('Director Technology','Director Technology'),
                ('Director','Director'),
                ('Vice President','Vice president'),
                ('President','President'),
                ('CEO','CEO'),
         )

    designationName = models.CharField(max_length=100, choices = JN, help_text = "Designation Name")

    def __str__(self):
        return self.designationName

class Information(models.Model):
    infoId = models.AutoField(primary_key = True)
    JN = (
                ('Trainee Engineer','Trainee Engineer'),
                ('Software Engineer','Software Engineer'),
                ('System Analyst','System Analyst'),
                ('Programmer Analyst','Programmer Analyst'),
                ('Senior Software Engineer','Senior Software Engineer'),
                ('Project Lead','Project Lead'),
                ('Project Manager','Project Manager'),
                ('Program Manager','Program Manager'),
                ('Architect','Architect'),
                ('Technical Specialist','Technical Specialist'),
                ('Deliver Manager','Deliver Manager'),
                ('Delivery Head','Delivery Head'),
                ('Business Analyst','Business Analyst'),
                ('Director Technology','Director Technology'),
                ('Director','Director'),
                ('Vice President','Vice president'),
                ('President','President'),
                ('CEO','CEO'),
         )

    companyName = models.CharField(max_length = 100,choices = JN, help_text = "Internship Name")
    designationDetails = models.CharField(max_length = 225, help_text = "Description")
    marks = models.IntegerField()

    def __str__(self):
        return self.companyName
        return self.designationDetails
