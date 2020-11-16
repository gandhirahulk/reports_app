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
from pandas import read_excel

from . import models
from .constants import *
from .fetch_fields import fetch_active_fields2

import base64

from django.core.files.base import ContentFile
# from datetime import datetime
from calendar import monthrange
def last_day_of_month(date_value):
    return date_value.replace(day = monthrange(date_value.year, date_value.month)[1])

def read_main_file():
    
    scope = ['https://spreadsheets.google.com/feeds']
    # gc = pygsheets.authorize(service_file='C:/Users/chirag.phor/Downloads/fourth-stock-291709-1cadc070c80b.xlsx')
    # emp_master = gc.open_by_url('https://docs.google.com/spreadsheets/d/1soEWcz-KwUAUR_8ua3xTHDHr0dfR5QEce4-gI0lnPyI/edit#gid=0')
    # wks3 = emp_master.worksheet_by_title("EmployeeMaster")
    # EmployeeMaster = wks3.get_as_df()
    EmployeeMaster = read_excel('C:/Users/chirag.phor/Downloads/fourth-stock-291709-1cadc070c80b.xlsx')
    for index,row in EmployeeMaster.iterrows():
        if row["LWD"]=="":
            EmployeeMaster.at[index,"LWD"]='31-Dec-2200'
    EmployeeMaster['DATE OF JOINING (DD/MM/YY)'] = pd.to_datetime(EmployeeMaster['DATE OF JOINING (DD/MM/YY)']).dt.strftime('%Y-%m-%d')
    EmployeeMaster.insert(5, "LWD_Remarks", EmployeeMaster['LWD'], True)
    EmployeeMaster['LWD'] = EmployeeMaster['LWD'].astype(str).str.replace("To be confirmed|Temporary Suspension|Data received from payroll team|to be cofirmed|Not Joined|to be confirmed|not joined|LWD is not available|Layoff cases|Absconded|LWd not available",'31-Dec-2200', regex=True, case = False)
    EmployeeMaster['LWD'] = pd.to_datetime(EmployeeMaster['LWD']).dt.strftime('%Y-%m-%d')
    EmployeeMaster.rename(columns = {'DEPARTMENT' : 'Department', 'FUNCTION /CATEGORY ' : 'Function_Category',
                                'TEAM':'Team','SUB TEAM':'Sub_team','STATE':'State','CITY':'City','DATE OF JOINING (DD/MM/YY)' : 'DOJ',
                                'LOCATION':'Location','VENDOR NAME':'VendorName'}, inplace = True)
    EmployeeMaster = EmployeeMaster.applymap(lambda s:s.lower() if type(s) == str else s)
    return EmployeeMaster

def return_frequency(filter_dict):
    for key in filter_dict:
        if key == "frequency":
            if len(list(filter_dict[key])) > 0:
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
    elif frequency=="MTD":
        today = date.today().strftime('%Y-%m-%d')
        dates= pd.date_range('2020-01-01',today , freq='1M')-pd.offsets.MonthBegin(1)
        date_value_list=dates.strftime("%Y-%m-%d").tolist()
    return date_value_list


def return_final_table(EmployeeMaster,date_value_list,report_type,frequency):
    from datetime import datetime
    lst = EmployeeMaster['VendorName'].unique().tolist()
    final_dataframe = pd.DataFrame(lst,columns =['VendorName']) 
    final_dataframe = final_dataframe.reindex(columns = final_dataframe.columns.tolist()) 
#     date_value_list.reverse()
    if report_type=="Monthly HC":
        if frequency=="MTD":
            for date_value in date_value_list:
                    given_date = datetime(year=2020, month=int(date_value.split('-')[1]), day=1).date()
                    end_of_month=last_day_of_month(given_date)
                    end_of_month=pd.to_datetime(end_of_month).strftime('%Y-%m-%d')
                    filtered_df=EmployeeMaster[(EmployeeMaster['DOJ']<=end_of_month) & (EmployeeMaster['LWD']>=date_value)]
                    print(date_value)
                    for index,row in final_dataframe.iterrows():
                        count=0
                        filter_dict={"VendorName":row["VendorName"]}
                        for key in filter_dict:
                            count=len(filtered_df[filtered_df[key]==filter_dict[key]])
                        final_dataframe.at[index,date_value]=count
    elif report_type=="Opening HC":
        for date_value in date_value_list:
                    given_date = datetime(year=2020, month=int(date_value.split('-')[1]), day=1).date()
                    end_of_month=last_day_of_month(given_date)
                    end_of_month=pd.to_datetime(end_of_month).strftime('%Y-%m-%d')
                    filtered_df=EmployeeMaster[(EmployeeMaster['DOJ']<=date_value) & (EmployeeMaster['LWD']>=date_value)]
                    print(date_value)
                    for index,row in final_dataframe.iterrows():
                        count=0
                        filter_dict={"VendorName":row["VendorName"]}
                        for key in filter_dict:
                            count=len(filtered_df[filtered_df[key]==filter_dict[key]])
                        final_dataframe.at[index,date_value]=count
                        
    elif report_type=="Closing HC":
        for date_value in date_value_list:
                    given_date = datetime(year=2020, month=int(date_value.split('-')[1]), day=1).date()
                    end_of_month=last_day_of_month(given_date)
                    end_of_month=pd.to_datetime(end_of_month).strftime('%Y-%m-%d')
                    filtered_df=EmployeeMaster[(EmployeeMaster['DOJ']<=end_of_month) & (EmployeeMaster['LWD']>=end_of_month)]
                    print(date_value)
                    for index,row in final_dataframe.iterrows():
                        count=0
                        filter_dict={"VendorName":row["VendorName"]}
                        for key in filter_dict:
                            count=len(filtered_df[filtered_df[key]==filter_dict[key]])
                        final_dataframe.at[index,date_value]=count
                        
    elif report_type=="Addition":
        for date_value in date_value_list:
                    given_date = datetime(year=2020, month=int(date_value.split('-')[1]), day=1).date()
                    end_of_month=last_day_of_month(given_date)
                    end_of_month=pd.to_datetime(end_of_month).strftime('%Y-%m-%d')
                    filtered_df=EmployeeMaster[(EmployeeMaster['DOJ']>=date_value) & (EmployeeMaster['DOJ']<=end_of_month)]
                    for index,row in final_dataframe.iterrows():
                        count=0
                        filter_dict={"VendorName":row["VendorName"]}
                        for key in filter_dict:
                            count=len(filtered_df[filtered_df[key]==filter_dict[key]])
                        final_dataframe.at[index,date_value]=count

    elif report_type=="Exit":
        for date_value in date_value_list:
                    given_date = datetime(year=2020, month=int(date_value.split('-')[1]), day=1).date()
                    end_of_month=last_day_of_month(given_date)
                    end_of_month=pd.to_datetime(end_of_month).strftime('%Y-%m-%d')
                    filtered_df=EmployeeMaster[(EmployeeMaster['LWD']>=date_value) & (EmployeeMaster['LWD']<=end_of_month)]
                    print(filtered_df.shape)
                    for index,row in final_dataframe.iterrows():
                        count=0
                        filter_dict={"VendorName":row["VendorName"]}
                        for key in filter_dict:
                            count=len(filtered_df[filtered_df[key]==filter_dict[key]])
                        final_dataframe.at[index,date_value]=count
    elif report_type=="Attrition Rate":
        for date_value in date_value_list:
                    given_date = datetime(year=2020, month=int(date_value.split('-')[1]), day=1).date()
                    end_of_month=last_day_of_month(given_date)
                    end_of_month=pd.to_datetime(end_of_month).strftime('%Y-%m-%d')
                    exit_count=len(EmployeeMaster[(EmployeeMaster['LWD']>=date_value) & (EmployeeMaster['LWD']<=end_of_month)])
                    opening_count=len(EmployeeMaster[(EmployeeMaster['DOJ']<=date_value) & (EmployeeMaster['LWD']>=date_value)])
                    closing_count=len(EmployeeMaster[(EmployeeMaster['DOJ']<=end_of_month) & (EmployeeMaster['LWD']>=end_of_month)])
                      
                    for index,row in final_dataframe.iterrows():
                        count=0
                        filter_dict={"VendorName":row["VendorName"]}
                        filtered_df = pd.DataFrame()
                        for key in filter_dict:
                            filtered_df=EmployeeMaster[EmployeeMaster[key]==filter_dict[key]]
                            exit_count=len(filtered_df[(filtered_df['LWD']>=date_value) & (filtered_df['LWD']<=end_of_month)])
                            opening_count=len(filtered_df[(filtered_df['DOJ']<=date_value) & (filtered_df['LWD']>=date_value)])
                            closing_count=len(filtered_df[(filtered_df['DOJ']<=end_of_month) & (filtered_df['LWD']>=end_of_month)])
                            try:
                                attrition=(exit_count/((opening_count+closing_count)/2))
                                
                            except:
                                attrition=0
                            count=len(filtered_df[filtered_df[key]==filter_dict[key]])
                        final_dataframe.at[index,date_value]=attrition*100
    
    return final_dataframe
    

def return_report_type(filter_dict):
    for key in filter_dict:
        if key=="report type":
            print("yes")
            if len(list(filter_dict[key])) >0:
                return list(filter_dict[key])[0]
            else:
                return "Monthly HC" 


def filtered_dataframe(EmployeeMaster,filter_dict):
    for key in filter_dict:
        if key=="dimensions":
            if type(filter_dict[key])==list:
                for dimensions in filter_dict[key]:
                    for dim in eval(dimensions):

                        if type(eval(dimensions)[dim])==list:
                            for name in eval(dimensions)[dim]:
                                name=name.lower()

                                EmployeeMaster=EmployeeMaster[EmployeeMaster[dim]==name]
    
    return EmployeeMaster   

@login_required(login_url=NOT_LOGIN)
def reports(request):
    if request.method == POST_METHOD:
        print(request.POST)
        query_dict_str = str(request.POST)
        # query_dict_str = query_dict_str.replace('<QueryDict:', '').replace('>', '')
        if  "Vendor" in query_dict_str:
            query_dict_str = query_dict_str.replace( "Vendor","VendorName") 
        query_dict_str=query_dict_str.replace('<QueryDict:','').replace('>','')
        query_dict_str=query_dict_str.replace('\\n','')
        print(query_dict_str)
        filter_dict=eval(query_dict_str)
        EmployeeMaster=read_main_file()
        frequency=return_frequency(filter_dict)
        print(frequency)
        date_value_list=return_date_list(frequency)
        print(date_value_list)
        report_type=return_report_type(filter_dict)
        print(report_type)
        filered_df=filtered_dataframe(EmployeeMaster,filter_dict)
        final_dataframe=return_final_table(filered_df,date_value_list,report_type,frequency)
        final_dataframe["VendorName"]= final_dataframe["VendorName"].str.upper().str.title()
        print(final_dataframe[:6])
        df_file = final_dataframe[:6].to_excel('static/df_to_excel/excel.xlsx')
        return render(request, TABLE_HTML, {'data_frame': final_dataframe[:6],'df_file':df_file})

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
