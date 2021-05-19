import csv
import time
import datetime

import dt as dt
import pandas as pd

def split_from_report():
    with open("/home/dilux/SenzMate/Bogawanthalawa/Analyzing/report.csv", "r", encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['Temp'] > '26.00']

    arr_list = []
    arr_date = []
    arr_month_date = []

    for row in rows:
        arr_list.append(row)
    # print(str(arr_list[0]).replace(",", ""))
    #     print(row)
    #     time.sleep(1)

        string = row['Time']
        print(string)
        temp2 = row['Temp']
        print(temp2)

        # size = len(string)
        # mod_string = string[:size - 3]
        # print(mod_string)

        date_time_obj = datetime.datetime.strptime(mod_string, '%Y-%m-%d %H:%M')
        val = str(date_time_obj.date())


    #     size2 = len(val)
    #     # date_only = val[size2 - 2:]
    #     date_only = val[size2 - 2 :]
    #     month_date = val[size2 - 5:]
    #     print(date_only +"  ---->  " + month_date)
    #     arr_date.append(date_only)
    #     arr_month_date.append(month_date)
    #
    # print(len(arr_month_date))
    # print(len(arr_date))
    # return arr_date, arr_month_date, arr_list
    #


def value_arr():
    arr_date = split_from_report()

    for i in range(len(arr_date)-1):
        if arr_date[i] == range(1,31):
            print(arr_date[i])
            print(5)

if __name__ == '__main__':
    split_from_report()
    # value_arr()