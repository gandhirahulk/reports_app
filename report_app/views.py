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
from .compute_results import *
import base64

from django.core.files.base import ContentFile
# from datetime import datetime
from calendar import monthrange


@login_required(login_url=NOT_LOGIN)
def reports(request):
    if request.method == POST_METHOD:
        print(request.POST)
        query_dict_str = str(request.POST)

        if "Vendor" in query_dict_str:
            query_dict_str = query_dict_str.replace("Vendor", "VendorName")
        query_dict_str = query_dict_str.replace(
            '<QueryDict:', '').replace('>', '')
        query_dict_str = query_dict_str.replace('\\n', '')
        filter_dict = eval(query_dict_str)

        # Reading master file
        start_time=time.time()
        EmployeeMaster = read_main_file()
        t1=time.time()-start_time
        print("Emp Read")
        print(t1)

        # Reading Frequency value
        start_time=time.time()
        frequency = return_frequency(filter_dict)
        print(time.time()-start_time)

        # Preparing Date list
        start_time=time.time()
        date_value_list = return_date_list(frequency,filter_dict)
        print(time.time()-start_time)

        # Reading Report Type
        start_time=time.time()
        report_type = return_report_type(filter_dict)
        print(time.time()-start_time)

        # Returning filtered dataframe based on dimensions
        start_time=time.time()
        filered_df = filtered_dataframe(EmployeeMaster, filter_dict)
        print(time.time()-start_time)
        

        # Returning final table
        final_dataframe = return_final_table(
            filered_df, date_value_list, report_type, frequency)
       

        # Dataframe post processing
        final_dataframe["VendorName"] = final_dataframe["VendorName"].str.upper().str.title()
        final_dataframe.style.set_properties(
            subset=["VendorName"], **{'text-align': 'left'})
        collist = final_dataframe.columns.tolist()

        if report_type != "Attrition rate":
            # if frequency == "MTD":
                final_dataframe[collist[1:]
                                ] = final_dataframe[collist[1:]].astype(int)
        if frequency == "MTD" or  frequency == "Quarterly YTD":
            df_dict = {}
            from datetime import datetime
            for col in collist[1:]:
                date_object = datetime.strptime(col, '%Y-%m-%d')
                df_dict[col] = date_object.strftime('%b %y')
            for col in final_dataframe.columns:
                for name in df_dict:
                    if name == col:
                        final_dataframe = final_dataframe.rename(
                            columns={col: df_dict[name]})

        end_time=time.time()
        print("------------------------")
        print("Time Taken by the engine:")
        print(end_time-start_time)
        print("------------------------")
        # print(final_dataframe[:4])
        df_file = final_dataframe.to_excel(
            'static/df_to_excel/final_output.xlsx',index=False)
        return render(request, TABLE_HTML, {'data_frame': final_dataframe, 'df_file': df_file})

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
                messages.add_message(
                    request, messages.WARNING, "Please Enter UID")
                return redirect('report_app:login')
            elif pwd == '':
                messages.add_message(
                    request, messages.WARNING, "Please Enter Password")
                return redirect('report_app:login')
            user = authenticate(request, username=usrname, password=pwd)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, "Login Successfull")
                return redirect('report_app:reports')

            else:
                messages.add_message(
                    request, messages.ERROR, "Invalid Credentials")
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
