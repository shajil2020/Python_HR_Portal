from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group

# Create your views here.
def index(request):
    if request.user.username == 'employee':
            return redirect('employee.dashboard')
    elif request.user.username == 'hr_admin':
            return redirect('hr.dashboard')
    else:
            return render(request,'login.html')

def user_login(request):

    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        elif request.user.groups.filter(name='HR').exists():
            return redirect('/hr/dashboard/')
        elif request.user.groups.filter(name='Employee').exists():
            return redirect('/employee/dashboard/')
        else:
            return redirect('/')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')

            elif user.groups.filter(name='HR').exists():
                return redirect('/hr/dashboard/')

            elif user.groups.filter(name='Employee').exists():
                return redirect('/employee/dashboard/')

            else:
                return redirect('/')
        else:
            return redirect('user_logout')

def user_logout(request):
    logout(request)
    return redirect('/')
