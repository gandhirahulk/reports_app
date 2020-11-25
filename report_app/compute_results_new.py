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
from pandas import read_excel
import base64
from django.core.files.base import ContentFile
# from datetime import datetime
from calendar import monthrange


def last_day_of_month(date_value):
    return date_value.replace(day=monthrange(date_value.year, date_value.month)[1])


def read_main_file():
    import pandas as pd
    from sqlalchemy import create_engine

    # follows django database settings format, replace with your own settings
    DATABASES = {
        'report': {
            'NAME': 'report',
            'USER': 'postgres',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1',
            'PORT': 5432,
        },
    }

    # choose the database to use
    db = DATABASES['report']

    # construct an engine connection string
    engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
        user=db['USER'],
        password=db['PASSWORD'],
        host=db['HOST'],
        port=db['PORT'],
        database=db['NAME'],
    )

    # create sqlalchemy engine
    engine = create_engine(engine_string)

    # read a table from database into pandas dataframe, replace "tablename" with your table name
    EmployeeMaster = pd.read_sql_table('report_app_employee', engine)
    for index, row in EmployeeMaster.iterrows():
        if row["lwd"] == "" or row["lwd"] == "None" or row["lwd"] is None:
            EmployeeMaster.at[index, "lwd"] = '31-Dec-2200'
    EmployeeMaster['doj'] = pd.to_datetime(
        EmployeeMaster['doj']).dt.strftime('%Y-%m-%d')
    EmployeeMaster.insert(5, "LWD_Remarks", EmployeeMaster['lwd'], True)
    EmployeeMaster['lwd'] = EmployeeMaster['lwd'].astype(str).str.replace(
        "To be confirmed|Temporary Suspension|Data received from payroll team|to be cofirmed|Not Joined|to be confirmed|not joined|LWD is not available|Layoff cases|Absconded|LWd not available",
        '31-Dec-2200', regex=True, case=False)
    EmployeeMaster['lwd'] = pd.to_datetime(
        EmployeeMaster['lwd']).dt.strftime('%Y-%m-%d')
    EmployeeMaster.rename(columns={'department': 'Department', 'function_category': 'Function_Category',
                                   'team': 'Team', 'sub_team': 'Sub_team', 'state': 'State', 'city': 'City',
                                   'doj': 'DOJ', 'lwd': 'LWD',
                                   'location': 'Location', 'vendor': 'VendorName'}, inplace=True)
    EmployeeMaster = EmployeeMaster.applymap(
        lambda s: s.lower() if type(s) == str else s)
    return EmployeeMaster


def return_frequency(filter_dict):
    for key in filter_dict:
        if key == "frequency":
            if len(list(filter_dict[key])) > 0:
                return list(filter_dict[key])[0]
            else:
                return "Monthly"


def quarter_cycle(quarter_list, date_value_list, year, datee):
    for quarter in quarter_list:
        if len(date_value_list) <= 7:
            prev = year
            first_day = datetime.date(prev, quarter[1][0], 1)
            last_day = datetime.date(prev, quarter[1][1], 1)
            if [first_day.strftime('%Y-%m-%d'), last_day.strftime('%Y-%m-%d')] not in date_value_list:
                if datee.date() > first_day:
                    date_value_list.append(
                        [first_day.strftime('%Y-%m-%d'), last_day.strftime('%Y-%m-%d')])
    return date_value_list


def return_date_list(frequency, filter_dict):
    from datetime import date
    from datetime import timedelta
    date_value_list = []
    today = date.today()
    if frequency == "Yesterday":
        yesterday = today - timedelta(days=1)
        date_value_list.append(yesterday.strftime('%Y-%m-%d'))
    elif frequency == "Week":
        today = date.today().strftime('%Y-%m-%d')
        dates = [datetime.datetime.strptime(
            today, '%Y-%m-%d') - datetime.timedelta(days=i) for i in range(7)]
        for day in dates:
            date_value_list.append(day.strftime('%Y-%m-%d').upper())

    elif frequency == "Fifteen":
        today = date.today().strftime('%Y-%m-%d')
        dates = [datetime.datetime.strptime(
            today, '%Y-%m-%d') - datetime.timedelta(days=i) for i in range(15)]
        for day in dates:
            date_value_list.append(day.strftime('%Y-%m-%d').upper())

    elif frequency == "MTD":
        today = date.today().strftime('%Y-%m-%d')
        dates = pd.date_range('2020-01-01', today,
                              freq='1M')-pd.offsets.MonthBegin(1)
        date_value_list = dates.strftime("%Y-%m-%d").tolist()
        from datetime import date
        from dateutil.relativedelta import relativedelta
        today = date.today()
        first_day = today.replace(day=1) + relativedelta(months=0)
        date_value_list.append(first_day.strftime('%Y-%m-%d'))

    elif frequency == "Annually":
        from datetime import date
        current_year = date(date.today().year, 1, 1)
        date_value_list.append(current_year.strftime('%Y-%m-%d'))
        for i in range(4):
            add = i+1
            date_value_list.append(
                date(date.today().year - add, 1, 1).strftime('%Y-%m-%d'))

    elif frequency == "Monthly YTD":
        for key in filter_dict:
            if key == "end_date":
                if type(filter_dict[key]) == list:
                    end_date = filter_dict[key][0]
        today = pd.to_datetime(end_date).strftime('%Y-%m-%d')
        dates = pd.date_range('2020-01-01', today,
                              freq='1M')-pd.offsets.MonthBegin(1)
        date_value_list = dates.strftime("%Y-%m-%d").tolist()

    elif frequency == "Quarterly YTD":
        # import datetime
        quarter_list = [("Q1", [1, 4]),
                        ("Q2", [4, 7]),
                        ("Q3", [7, 10]),
                        ("Q4", [10, 12])]
        quarter_start = ""
        for key in filter_dict:
            if key == "end_date":
                if type(filter_dict[key]) == list:
                    end_date = filter_dict[key][0]
                    datee = datetime.datetime.strptime(end_date, "%Y-%m-%d")

                    for quarter in quarter_list:
                        if int(datee.month) >= int(quarter[1][0]) and int(datee.month) < int(quarter[1][1]):
                            quarter_start = quarter[0]
                            first_day = datetime.date(
                                datee.year, quarter[1][0], 1)
                            last_day = datetime.date(
                                datee.year, quarter[1][1], 1)
                            date_value_list.append(
                                [first_day.strftime('%Y-%m-%d'), last_day.strftime('%Y-%m-%d')])

                    for quarter in quarter_list:
                        if len(date_value_list) <= 7:
                            prev = datee.year
                            first_day = datetime.date(prev, quarter[1][0], 1)
                            last_day = datetime.date(prev, quarter[1][1], 1)
                            if [first_day.strftime('%Y-%m-%d'), last_day.strftime('%Y-%m-%d')] not in date_value_list:
                                if datee.date() > first_day:
                                    date_value_list.append(
                                        [first_day.strftime('%Y-%m-%d'), last_day.strftime('%Y-%m-%d')])

                    date_value_list = quarter_cycle(
                        quarter_list, date_value_list, datee.year-1, datee)
                    date_value_list = quarter_cycle(
                        quarter_list, date_value_list, datee.year-2, datee)

    return date_value_list


def preparing_final_dataframe(final_dataframe, filtered_df,date_value):
    for index, row in final_dataframe.iterrows():
        count = 0
        filter_dict_vendor = {"VendorName": row["VendorName"]}
        for key in filter_dict_vendor:
            count = len(filtered_df[filtered_df[key]
                                    == filter_dict_vendor[key]])
        final_dataframe.at[index, date_value] = count
    return final_dataframe


def return_final_table(EmployeeMaster, date_value_list, report_type, frequency):
    from datetime import datetime
    lst = EmployeeMaster['VendorName'].unique().tolist()
    final_dataframe = pd.DataFrame(lst, columns=['VendorName'])
    final_dataframe = final_dataframe.reindex(
        columns=final_dataframe.columns.tolist())
#     date_value_list.reverse()
    if report_type == "Monthly HC":
        if frequency == "MTD":
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value.split('-')[1]), day=1).date()
                end_of_month = last_day_of_month(given_date)
                end_of_month = pd.to_datetime(
                    end_of_month).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] <= end_of_month) & (
                    EmployeeMaster['LWD'] >= date_value)]

                final_dataframe = preparing_final_dataframe(
                    final_dataframe, filtered_df,date_value)
    elif report_type == "Opening HC":
        if frequency != "Quarterly YTD":
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value.split('-')[1]), day=1).date()
                end_of_month = last_day_of_month(given_date)
                end_of_month = pd.to_datetime(
                    end_of_month).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] <= date_value) & (
                    EmployeeMaster['LWD'] >= date_value)]

                final_dataframe = preparing_final_dataframe(
                    final_dataframe, filtered_df,date_value)

        else:
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value[0].split('-')[1]), day=1).date()
                if frequency == "Annually":
                    from datetime import date
                    year = int(date_value.split('-')[0])
                    end_of_month = pd.to_datetime(
                        date(year, 12, 31).strftime('%Y-%m-%d'))
                else:
                    end_of_month = pd.to_datetime(
                        date_value[1]).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] <= date_value[0]) & (
                    EmployeeMaster['LWD'] >= date_value[0])]

                final_dataframe = preparing_final_dataframe(
                    final_dataframe, filtered_df,date_value)

    elif report_type == "Closing HC":
        if frequency != "Quarterly YTD":
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value.split('-')[1]), day=1).date()
                if frequency == "Annually":
                    from datetime import date
                    year = int(date_value.split('-')[0])
                    end_of_month = pd.to_datetime(
                        date(year, 12, 31).strftime('%Y-%m-%d'))
                else:
                    end_of_month = last_day_of_month(given_date)
                    end_of_month = pd.to_datetime(
                        end_of_month).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] <= end_of_month) & (
                    EmployeeMaster['LWD'] >= end_of_month)]

                for index, row in final_dataframe.iterrows():
                    count = 0
                    filter_dict_vendor = {"VendorName": row["VendorName"]}
                    for key in filter_dict_vendor:
                        count = len(
                            filtered_df[filtered_df[key] == filter_dict_vendor[key]])
                    final_dataframe.at[index, date_value] = count
        else:
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value[0].split('-')[1]), day=1).date()
                end_of_month = pd.to_datetime(
                    date_value[1]).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] <= end_of_month) & (
                    EmployeeMaster['LWD'] >= end_of_month)]
                final_dataframe = preparing_final_dataframe(
                    final_dataframe, filtered_df,date_value)

    elif report_type == "Addition":
        if frequency == "Quarterly YTD":
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value[0].split('-')[1]), day=1).date()
                end_of_month = pd.to_datetime(
                    date_value[1]).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] >= date_value[0]) & (
                    EmployeeMaster['DOJ'] <= end_of_month)]
                for index, row in final_dataframe.iterrows():
                    count = 0
                    filter_dict_vendor = {"VendorName": row["VendorName"]}
                    for key in filter_dict_vendor:
                        count = len(
                            filtered_df[filtered_df[key] == filter_dict_vendor[key]])
                    final_dataframe.at[index, date_value[0]] = count
        else:
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value.split('-')[1]), day=1).date()
                if frequency == "Annually":
                    from datetime import date
                    year = int(date_value.split('-')[0])
                    end_of_month = pd.to_datetime(
                        date(year, 12, 31).strftime('%Y-%m-%d'))
                else:
                    end_of_month = last_day_of_month(given_date)
                    end_of_month = pd.to_datetime(
                        end_of_month).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] >= date_value) & (
                    EmployeeMaster['DOJ'] <= end_of_month)]
                final_dataframe = preparing_final_dataframe(
                    final_dataframe, filtered_df,date_value)

    elif report_type == "Net Addition":

        for date_value in date_value_list:
            given_date = datetime(year=2020, month=int(
                date_value.split('-')[1]), day=1).date()
            end_of_month = last_day_of_month(given_date)
            end_of_month = pd.to_datetime(end_of_month).strftime('%Y-%m-%d')
            filtered_df = EmployeeMaster[(EmployeeMaster['DOJ'] >= date_value) & (
                EmployeeMaster['DOJ'] <= end_of_month)]
            for index, row in final_dataframe.iterrows():
                count = 0
                filter_dict_vendor = {"VendorName": row["VendorName"]}
                for key in filter_dict_vendor:
                    count = len(
                        filtered_df[filtered_df[key] == filter_dict_vendor[key]])
                    final_dataframe.at[index, date_value] = len(filtered_df)

        final_dataframe.loc[len(final_dataframe.index)] = final_dataframe.sum(
            numeric_only=True, axis=0)
    elif report_type == "Exit":
        if frequency != "Quarterly YTD":
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value.split('-')[1]), day=1).date()
                if frequency == "Annually":
                    from datetime import date
                    year = int(date_value.split('-')[0])
                    end_of_month = pd.to_datetime(
                        date(year, 12, 31).strftime('%Y-%m-%d'))
                else:
                    end_of_month = last_day_of_month(given_date)
                    end_of_month = pd.to_datetime(
                        end_of_month).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['LWD'] >= date_value) & (
                    EmployeeMaster['LWD'] <= end_of_month)]
                final_dataframe = preparing_final_dataframe(
                    final_dataframe, filtered_df,date_value)

        else:
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value[0].split('-')[1]), day=1).date()
                # end_of_month=last_day_of_month(given_date)
                end_of_month = pd.to_datetime(
                    date_value[1]).strftime('%Y-%m-%d')
                filtered_df = EmployeeMaster[(EmployeeMaster['LWD'] >= date_value[0]) & (
                    EmployeeMaster['LWD'] <= end_of_month)]
                final_dataframe = preparing_final_dataframe(
                    final_dataframe, filtered_df,date_value)

    elif report_type == "Attrition rate":
        if frequency != "Quarterly YTD":
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value.split('-')[1]), day=1).date()
                if frequency == "Annually":
                    from datetime import date
                    year = int(date_value.split('-')[0])
                    end_of_month = pd.to_datetime(
                        date(year, 12, 31).strftime('%Y-%m-%d'))
                else:
                    end_of_month = last_day_of_month(given_date)
                    end_of_month = pd.to_datetime(
                        end_of_month).strftime('%Y-%m-%d')

                for index, row in final_dataframe.iterrows():
                    count = 0
                    filter_dict_vendor = {"VendorName": row["VendorName"]}
                    filtered_df = pd.DataFrame()
                    for key in filter_dict_vendor:
                        filtered_df = EmployeeMaster[EmployeeMaster[key]
                                                     == filter_dict_vendor[key]]
                        exit_count = len(filtered_df[(filtered_df['LWD'] >= date_value) & (
                            filtered_df['LWD'] <= end_of_month)])
                        opening_count = len(filtered_df[(filtered_df['DOJ'] <= date_value) & (
                            filtered_df['LWD'] >= date_value)])
                        closing_count = len(filtered_df[(filtered_df['DOJ'] <= end_of_month) & (
                            filtered_df['LWD'] >= end_of_month)])
                        try:
                            attrition = (
                                exit_count/((opening_count+closing_count)/2))

                        except:
                            attrition = 0
                        count = len(
                            filtered_df[filtered_df[key] == filter_dict_vendor[key]])
                    final_dataframe.at[index,
                                       date_value] = "{:.0%}".format(attrition)
        else:
            for date_value in date_value_list:
                given_date = datetime(year=2020, month=int(
                    date_value[0].split('-')[1]), day=1).date()

                end_of_month = pd.to_datetime(
                    date_value[1]).strftime('%Y-%m-%d')
                for index, row in final_dataframe.iterrows():
                    count = 0
                    filter_dict_vendor = {"VendorName": row["VendorName"]}
                    filtered_df = pd.DataFrame()
                    for key in filter_dict_vendor:
                        filtered_df = EmployeeMaster[EmployeeMaster[key]
                                                     == filter_dict_vendor[key]]
                        exit_count = len(filtered_df[(filtered_df['LWD'] >= date_value[0]) & (
                            filtered_df['LWD'] <= end_of_month)])
                        opening_count = len(filtered_df[(filtered_df['DOJ'] <= date_value[0]) & (
                            filtered_df['LWD'] >= date_value[0])])
                        closing_count = len(filtered_df[(filtered_df['DOJ'] <= end_of_month) & (
                            filtered_df['LWD'] >= end_of_month)])
                        try:
                            attrition = (
                                exit_count/((opening_count+closing_count)/2))

                        except:
                            attrition = 0
                        count = len(
                            filtered_df[filtered_df[key] == filter_dict_vendor[key]])
                    final_dataframe.at[index, date_value[0]
                                       ] = "{:.0%}".format(attrition)

    return final_dataframe


def return_report_type(filter_dict):
    for key in filter_dict:
        if key == "report type":

            if len(list(filter_dict[key])) > 0:
                return list(filter_dict[key])[0]
            else:
                return "Monthly HC"


def filtered_dataframe(EmployeeMaster, filter_dict):

    for key in filter_dict:
        if key == "dimensions":
            if type(filter_dict[key]) == list:
                for dimensions in filter_dict[key]:
                    for dim in eval(dimensions):

                        if type(eval(dimensions)[dim]) == list:
                            for name in eval(dimensions)[dim]:

                                name = name.replace(',', '')
                                name = name.lower()
                                EmployeeMaster = EmployeeMaster[EmployeeMaster[dim] == name]

    return EmployeeMaster
