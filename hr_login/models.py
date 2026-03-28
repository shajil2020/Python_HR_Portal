from django.db import models
from employee_login.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)
    punch_in = models.TimeField(null=True,blank=True)
    punch_out = models.TimeField(null=True,blank=True)
    APPROVAL_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    approval_status = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.emp_name} - {self.date}"

class Leaves(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    LEAVE_TYPE_CHOICES = [
        ('CL', 'Casual Leave'),
        ('SL', 'Sick Leave'),
        ('PL', 'Paid Leave'),
    ]
    leave_type = models.CharField(
        max_length=2,
        choices=LEAVE_TYPE_CHOICES
    )
    start_date = models.DateField()
    end_date = models.DateField()
    leave_days = models.IntegerField()
    reason = models.TextField()

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.emp_name} - {self.leave_type} ({self.start_date} to {self.end_date})"

class Holiday(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    date = models.DateField()
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date',)

    def __str__(self):
        return f"{self.name} - {self.date}"
