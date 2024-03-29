# Generated by Django 2.2.1 on 2019-07-11 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('yearId', models.AutoField(primary_key=True, serialize=False)),
                ('yearName', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branche',
            fields=[
                ('branchId', models.AutoField(primary_key=True, serialize=False)),
                ('branchName', models.CharField(choices=[('computer', 'computer'), ('Mech', 'Mech'), ('civil', 'civil'), ('ETC', 'Etc')], help_text='Branch Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semesterid', models.AutoField(primary_key=True, serialize=False)),
                ('semesterName', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollNo', models.IntegerField(primary_key=True, serialize=False)),
                ('percent', models.IntegerField(help_text='Percentage', null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], help_text='Gender', max_length=10, null=True)),
                ('branchId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentBranchId', to='Applicant_app.Branche')),
                ('semesterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentSemesterId', to='Applicant_app.Semester')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AcademicYearId', to='Applicant_app.AcademicYear')),
            ],
            options={
                'ordering': ['-user'],
                'permissions': (('is_student', 'is_student'),),
            },
        ),
    ]
