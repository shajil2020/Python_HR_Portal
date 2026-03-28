from django.contrib import admin
from .models import Employee
from .models import Department, Designation

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Designation)