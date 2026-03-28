from django.db import models
from role.models import Roles
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    emp_name = models.CharField(max_length=100)
    emp_mobile = models.CharField(max_length=10)
    emp_role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    # ✅ NEW FIELDS
    emp_image = models.ImageField(upload_to='employees/', null=True, blank=True)
    emp_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    emp_designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)

    QUALIFICATION_CHOICES = [
        ('SSLC', 'SSLC'),
        ('PLUS_TWO', 'Plus Two'),
        ('DIPLOMA', 'Diploma'),
        ('UG', 'Under Graduate'),
        ('PG', 'Post Graduate'),
        ('PHD', 'PhD'),
    ]

    emp_highest_qualification = models.CharField(
        max_length=20,
        choices=QUALIFICATION_CHOICES,
        null=True,
        blank=True
    )

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    emp_gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )

    emp_technical_skills = models.TextField(null=True, blank=True)
    emp_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.emp_name