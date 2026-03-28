from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from employee_login.models import Employee
from django.contrib.auth.models import User, Group
from employee_login.models import Department, Designation
from hr_login.models import Attendance,Leaves,Holiday
from django.contrib import messages
from datetime import datetime

@login_required(login_url='/')
def dashboard(request):
   if request.user.is_authenticated and request.user.is_superuser == False:
        total_employees = Employee.objects.count()
        total_count = Holiday.objects.count()
        userDet = {
           'firstName':request.user.first_name,
           'username':request.user.username,
           'isSuperuser':request.user.is_superuser,
           'total_employees':total_employees,
           'total_count':total_count,
        }
        return render(request, 'hr_users/dashboard.html',userDet)
   else:
        return redirect('/')
   
@login_required(login_url='/')
def myProfile(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'hr_users/myprofile.html', {
        'emp':emp,
    })

@login_required(login_url='/')   
def employeeList(request):
   employeeList = Employee.objects.all()
   return render(request, 'hr_users/employees.html' , {
               'employeeList': employeeList,
   })

@login_required(login_url='/')
def employeeCreate(request):
    departments = Department.objects.all()
    designations = Designation.objects.all()

    return render(request, 'hr_users/employeeForm.html', {
        'departments': departments,
        'designations': designations
    })

@login_required(login_url='/')
def employeeSave(request):
    if request.method == "POST":
        username = request.POST.get('empUserName')
        password = request.POST.get('empPassword')
        email =  request.POST.get('empEmail')
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        group = Group.objects.get(name='Employee')
        user.groups.add(group)
        dept_id = request.POST.get('empDept')
        des_id = request.POST.get('empDesig')
        Employee.objects.create(
            emp_role_id =1,
            emp_name=request.POST.get('empName'),
            emp_mobile=request.POST.get('empMobile'),
            emp_gender=request.POST.get('gender'),
            emp_address=request.POST.get('empAddress'),
            emp_highest_qualification=request.POST.get('empQuali'),
            emp_technical_skills=request.POST.get('empSkills'),
            emp_department = Department.objects.get(id=dept_id),
            emp_designation = Designation.objects.get(id=des_id),
            emp_image = request.POST.get('empImage'),
        )
        messages.success(request, "Saved successfully ✅")
        return redirect('hr.employee_list')
    
@login_required(login_url='/')   
def employeeEdit(request, id):
    emp = Employee.objects.get(id=id)
    departments = Department.objects.all()
    designations = Designation.objects.all()

    return render(request, 'hr_users/editEmployee.html', {
        'departments': departments,
        'designations': designations,
        'emp':emp,
    })

def employeeUpdate(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == "POST":
        dept_id = request.POST.get('empDept')
        des_id = request.POST.get('empDesig')
        emp.emp_name = request.POST.get('empName')
        emp.emp_gender = request.POST.get('gender')
        emp.emp_mobile = request.POST.get('empMobile')
        emp.emp_address=request.POST.get('empAddress')
        emp.emp_highest_qualification = request.POST.get('empQuali')
        emp.emp_technical_skills = request.POST.get('empSkills')
        emp.emp_department = Department.objects.get(id=dept_id)
        emp.emp_designation = Designation.objects.get(id=des_id)

        if request.FILES.get('empImage'): 
            emp.emp_image = request.FILES.get('empImage')

        emp.save()

        user = User.objects.get(id=emp.user.id)
        first_name = request.POST.get('empName')
        email = request.POST.get('empEmail')

        if first_name:
            emp.user.first_name = first_name

        if email:
            emp.user.email = email

        emp.user.save()
    messages.success(request, "Update successfully ✅")
    return redirect('hr.employee_list')

def attendance(request):
   attendanceList = Attendance.objects.all()
   return render(request, 'hr_users/attendance.html' , {
               'attendanceList': attendanceList,
   })

def createAttendance(request):
    if request.user.groups.filter(name='Employee').exists():
        employeeList = Employee.objects.filter(user=request.user)
    else:
        employeeList = Employee.objects.all()
    return render(request, 'hr_users/createAttendance.html' , {
               'employeeList': employeeList,
   })

@login_required(login_url='/')
def saveAttendance(request):
    if request.method=='POST':
        emp_id = request.POST.get('empName')
        attendance_date=request.POST.get('attendance_date')
        attendance_punch_in = request.POST.get('attendance_punch_in')
        attendance_punch_out = request.POST.get('attendance_punch_out')
        approval_status = request.POST.get('status', 'Pending')
        if not emp_id:
            messages.error(request, "Please select employee..!")
            return redirect('hr.create_attendance')
        if not attendance_date:
            messages.error(request, "Please select Date..!")
            return redirect('hr.create_attendance')
        if not attendance_punch_in:
            messages.error(request, "Please select Punch In..!")
            return redirect('hr.create_attendance')
        if not attendance_punch_out:
            messages.error(request, "Please select Punch Out..!")
            return redirect('hr.create_attendance')
        try:
            date_obj = datetime.strptime(attendance_date, "%Y-%m-%d").date()
        except Exception:
            messages.error(request, "Invalid date format")
            return redirect('hr.create_attendance')
        
        Attendance.objects.create(
            employee=  Employee.objects.get(id=emp_id),
            date= date_obj,
            punch_in=attendance_punch_in,
            punch_out= attendance_punch_out,
            approval_status= approval_status,
        )
    messages.success(request, "Saved successfully ✅")
    return redirect('hr.employee_attendance')

def leaves(request):
    if request.user.groups.filter(name='Employee').exists():
        leavesList = Leaves.objects.filter(employee__user=request.user)
    else:
        leavesList = Leaves.objects.all()
    return render(request, 'hr_users/leaveList.html' , {
               'leavesList': leavesList,
   })

def createLeave(request):
    if request.user.groups.filter(name='Employee').exists():
        employeeList = Employee.objects.filter(user=request.user)
    else:
        employeeList = Employee.objects.all()
    return render(request, 'hr_users/createLeave.html' , {
               'employeeList': employeeList,
   })


def holyDayList(request):
    holyDayList = Holiday.objects.all()
    return render(request, 'hr_users/holidayList.html' , {
               'holyDayList': holyDayList,
   })

@login_required(login_url='/')
def createHoliday(request):
    return render(request, 'hr_users/createHoliday.html')

@login_required(login_url='/')
def saveHolyday(request):
    if request.method=='POST':
        Holiday.objects.create(
            name=request.POST.get('holiday_name'),
            date=request.POST.get('holiday_date'),
            description= request.POST.get('description'),
        )
    messages.success(request, "Saved successfully ✅") 
    return redirect('hr.holyDayList')

def saveLeaves(request):
    emp_id = request.POST.get('empName')
    leave_type = request.POST.get('leave_type')
    start_date= request.POST.get('leave_start_date'),

    if not emp_id:
        messages.error(request, "Please select employee..!")
        return redirect('hr.create_leave')
    if not leave_type:
        messages.error(request, "Please select leave type..!")
        return redirect('hr.create_leave')    
    if not start_date:
        messages.error(request, "Please select Start Date..!")
        return redirect('hr.create_leave')
       
    if request.method=='POST':
        Leaves.objects.create(
            employee=Employee.objects.get(id=emp_id),
            leave_type= leave_type,
            start_date= start_date,
            end_date= request.POST.get('leave_end_date'),
            leave_days= request.POST.get('leave_days'),
            reason= request.POST.get('leave_reason'),
            status= request.POST.get('status'),
        )
    messages.success(request, "Saved successfully ✅") 
    return redirect('hr.leaves')

