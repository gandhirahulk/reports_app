import datetime
import json
import urllib

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from . import models
from .constants import *
from .fetch_fields import fetch_active_fields2

import base64

from django.core.files.base import ContentFile


@login_required(login_url=NOT_LOGIN)
def payroll(request):
    if request.method == POST_METHOD:
        print(request.POST)
        message = 'lol'
        # return render(request, DASHBOARD_HTML, {'employees': getattr(models, EMPLOYEES).objects.filter(status=ACTIVE)})
        # return JsonResponse(data, safe=False)
        return HttpResponse(json.dumps({'message': message}))

    field_list = [EMPLOYEES, VENDORS, STATES, LOCATIONS, GENDERS, TEAMS, FUNCTIONS, REPORT_TYPES, FREQUENCIES,
                  DIMENSIONS,CITIES,SUB_TEAMS]
    active_fields = fetch_active_fields2(field_list)
    return render(request, REPORTS_HTML, active_fields)


def csp_login(request):
    if request.method == "POST":
        if request.POST.get('username') != None or request.POST.get('username') != '':
            usrname = request.POST.get('username')
            pwd = request.POST.get('password')
            if usrname == '':
                messages.add_message(request, messages.WARNING, "Please Enter UID")
                return redirect('report_app:login')
            elif pwd == '':
                messages.add_message(request, messages.WARNING, "Please Enter Password")
                return redirect('report_app:login')
            user = authenticate(request, username=usrname, password=pwd)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, "Login Successfull")
                return redirect('report_app:payroll')

            else:
                messages.add_message(request, messages.ERROR, "Invalid Credentials")
                return redirect('report_app:login')
    return render(request, 'Login.html')

@login_required(login_url='/notlogin/')
def csp_logout(request):
    logout(request)
    return redirect('report_app:login')


def notlogin(request):
    return render(request, 'timeout.html')

@login_required(login_url='/notlogin/')
def change_password(request):
    
    selected_user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        
        pwd = request.POST.get('new_password2')
        selected_user.password = pwd
        selected_user.set_password(selected_user.password)
        selected_user.save()
        return render(request, 'registration/password_reset_complete.html')
    return render(request, 'registration/password_change.html')
    
