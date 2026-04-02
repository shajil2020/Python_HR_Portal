from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from employee_login.models import Employee
from hr_login.models import Attendance,Leaves,Holiday

# Create your views here.
@never_cache
@login_required
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
        total_employees = Employee.objects.count()
        total_holiday = Holiday.objects.count()
        total_leave = Employee.objects.filter(user=request.user).count()
        userDet = {
           'firstName':request.user.first_name,
           'username':request.user.username,
           'isSuperuser':request.user.is_superuser,
           'total_employees':total_employees,
           'total_holiday':total_holiday,
           'total_leave':total_leave,
        }
        return render(request, 'employee/dashboard.html',userDet)
    else:
        return redirect('/')
    
@login_required(login_url='/')        
def myProfile(request):
      if request.user.is_authenticated and request.user.is_superuser == False:
         return render(request, 'employee/myprofile.html')
      else:
        return redirect('/')
      
@login_required(login_url='/')      
def attendance(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
      return HttpResponse("Employeeattendance")
    else:
        return redirect('/')
@login_required(login_url='/')    
def leaves(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
      return HttpResponse("Employeeleaves")
    else:
        return redirect('/')
    
@login_required(login_url='/')   
def salarySlip(request):
    if request.user.is_authenticated and request.user.is_superuser == False:
      return HttpResponse("Employee salary_slip")
    else:
      return redirect('/')

