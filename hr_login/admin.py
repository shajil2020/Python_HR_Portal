from django.contrib import admin
from .models import Attendance,Leaves,Holiday

# Register your models here.
admin.site.register(Attendance)
admin.site.register(Leaves)
admin.site.register(Holiday)

