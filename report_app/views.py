import datetime
import json
import urllib
import pandas as pd
import numpy as np
import requests
import pygsheets
import io
from collections import Counter
import datetime
import schedule
import time
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

def read_main_file():
    
    scope = ['https://spreadsheets.google.com/feeds']
    gc = pygsheets.authorize(service_file='C:/Users/patel.vaishakhi/Downloads/fourth-stock-291709-1cadc070c80b.json')
    emp_master = gc.open_by_url('https://docs.google.com/spreadsheets/d/1soEWcz-KwUAUR_8ua3xTHDHr0dfR5QEce4-gI0lnPyI/edit#gid=0')
    wks3 = emp_master.worksheet_by_title("EmployeeMaster")
    EmployeeMaster = wks3.get_as_df()
    for index,row in EmployeeMaster.iterrows():
        if row["LWD"]=="":
            EmployeeMaster.at[index,"LWD"]='31-Dec-2200'
    EmployeeMaster['DATE OF JOINING (DD/MM/YY)'] = pd.to_datetime(EmployeeMaster['DATE OF JOINING (DD/MM/YY)']).dt.strftime('%Y-%m-%d')
    EmployeeMaster.insert(5, "LWD_Remarks", EmployeeMaster['LWD'], True)
    EmployeeMaster['LWD'] = EmployeeMaster['LWD'].str.replace("To be confirmed|Temporary Suspension|Data received from payroll team|to be cofirmed|Not Joined|to be confirmed|not joined|LWD is not available|Layoff cases|Absconded|LWd not available",'31-Dec-2200', regex=True, case = False)
    
    EmployeeMaster.rename(columns = {'DEPARTMENT' : 'Department', 'FUNCTION /CATEGORY ' : 'Function_Category',
                                'TEAM':'Team','SUB TEAM':'Sub_team','STATE':'State','CITY':'City','DATE OF JOINING (DD/MM/YY)' : 'DOJ',
                                'LOCATION':'Location','VENDOR NAME':'VendorName'}, inplace = True)
    EmployeeMaster = EmployeeMaster.applymap(lambda s:s.lower() if type(s) == str else s)
    return EmployeeMaster

def return_frequency(filter_dict):
    for key in filter_dict:
        if key=="frequency":
            if len(list(filter_dict[key])) >0:
                return list(filter_dict[key])[0]
            else:
                return "Monthly"

def return_date_list(frequency):
    from datetime import date 
    from datetime import timedelta 
    date_value_list=[]
    today = date.today()
    if frequency=="Yesterday":
        yesterday = today - timedelta(days = 1)
        date_value_list.append(yesterday.strftime('%Y-%m-%d'))
    elif frequency=="Week":
        today = date.today().strftime('%Y-%m-%d')
        dates = [datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days=i) for i in range(7)]
        for day in dates:
            date_value_list.append(day.strftime('%Y-%m-%d').upper())
    elif frequency=="Fifteen":
        today = date.today().strftime('%Y-%m-%d')
        dates = [datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days=i) for i in range(15)]
        for day in dates:
            date_value_list.append(day.strftime('%Y-%m-%d').upper())
    elif frequency=="Monthly":
        today = date.today().strftime('%Y-%m-%d')
        dates = [datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days=i) for i in range(30)]
        for day in dates:
            date_value_list.append(day.strftime('%Y-%m-%d').upper())
    return date_value_list

def return_final_table(EmployeeMaster,date_value_list,test):
    lst = EmployeeMaster['VendorName'].unique().tolist()
    final_dataframe = pd.DataFrame(lst,columns =['VendorName']) 
    final_dataframe = final_dataframe.reindex(columns = final_dataframe.columns.tolist()) 
    for date_val in date_value_list:
        for index,row in final_dataframe.iterrows():
                count=0
                f_dict={"VendorName":row["VendorName"]}
                for key in f_dict:
                    count=len(test[test[key]==f_dict[key]])

                final_dataframe.at[index,date_val]=count
    return final_dataframe

def return_report_type(filter_dict):
    for key in filter_dict:
        if key=="report type":
            print("yes")
            if len(list(filter_dict[key])) >0:
                return list(filter_dict[key])[0]
            else:
                return "Monthly HC" 

def filtered_dataframe(report_type,date_value_list,emp_master,filter_dict):
    if report_type=="Monthly HC":
        if len(date_value_list)==1:
            for date_value in date_value_list:
                filtered_df=emp_master[(emp_master['DOJ']<=date_value) & (emp_master['LWD']>=date_value)]
        else:
            filtered_df=emp_master[(emp_master['DOJ']<=date_value_list[0]) & (emp_master['LWD']>=date_value_list[-1])]
    filtered_df = filtered_df.applymap(lambda s:s.lower() if type(s) == str else s)
    for key in filter_dict:
        if key=="dimensions":
            if type(filter_dict[key])==list:
                for dimensions in filter_dict[key]:
                    for dim in eval(dimensions):
                        
                        if type(eval(dimensions)[dim])==list:
                            for name in eval(dimensions)[dim]:
                                name=name.lower()
                                
                                filtered_df=filtered_df[filtered_df[dim]==name]
    
    return filtered_df

@login_required(login_url=NOT_LOGIN)
def reports(request):
    if request.method == POST_METHOD:
        print(request.POST)
        message = 'lol'
        # return render(request, DASHBOARD_HTML, {'employees': getattr(models, EMPLOYEES).objects.filter(status=ACTIVE)})
        # return JsonResponse(data, safe=False)
        query_dict_str=str(request.POST)
        query_dict_str=query_dict_str.replace('<QueryDict:','').replace('>','')
        query_dict_str=query_dict_str.replace('\\n','')
        print(query_dict_str)
        filter_dict=eval(query_dict_str)
        EmployeeMaster=read_main_file()
        frequency=return_frequency(filter_dict)
        print(frequency)
        date_value_list=return_date_list(frequency)
        report_type=return_report_type(filter_dict)
        test=filtered_dataframe(report_type,date_value_list,EmployeeMaster,filter_dict)
        final_dataframe=return_final_table(EmployeeMaster,date_value_list,test)
        print(final_dataframe[:5])


        field_list = [EMPLOYEES]
        active_fields = fetch_active_fields2(field_list)
        return HttpResponse(json.dumps({'message': message}))

    field_list = [EMPLOYEES, VENDORS, STATES, LOCATIONS, GENDERS, TEAMS, FUNCTIONS, REPORT_TYPES, FREQUENCIES,
                  DIMENSIONS, CITIES, SUB_TEAMS, REGIONS, CTC_SLABS, EXIT_TYPES, AGES, EMP_TYPES, TENURES, ENTITIES]
    active_fields = fetch_active_fields2(field_list)
    return render(request, REPORT_HTML, active_fields)


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
                return redirect('report_app:reports')

            else:
                messages.add_message(request, messages.ERROR, "Invalid Credentials")
                return redirect('report_app:login')
    return render(request, 'login.html')


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
