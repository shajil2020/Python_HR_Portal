"""
URL configuration for hrportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hr/dashboard/', views.dashboard, name='hr.dashboard'),
    path('hr/my_profile/<int:id>/',views.myProfile, name='hr.my_profile'),
    path('hr/employee',views.employeeList, name='hr.employee_list'),
    path('hr/create_employee',views.employeeCreate, name='hr.employee_create'),
    path('hr/save_employee',views.employeeSave, name='hr.save_employee'),
    path('hr/edit_employee/<int:id>/', views.employeeEdit, name='employee_edit'),
    path('hr/update_employee/<int:id>/', views.employeeUpdate, name='hr.employee_update'),
    path('hr/attendance',views.attendance, name ='hr.employee_attendance'),
    path('hr/create_attendance',views.createAttendance, name ='hr.create_attendance'),
    path('hr/save_attendance',views.saveAttendance, name='hr.save_attendance'),
    path('hr/leaves',views.leaves, name ='hr.leaves'),
    path('hr/create_leaves',views.createLeave, name ='hr.create_leave'),
    path('hr/save_leaves',views.saveLeaves, name='hr.save_leaves'),
    path('hr/holyDayList',views.holyDayList, name ='hr.holyDayList'),
    path('hr/create_holyDay',views.createHoliday, name ='hr.create_holyDay'),
    path('hr/save_holyDay',views.saveHolyday, name='hr.save_holyDay'),
]
