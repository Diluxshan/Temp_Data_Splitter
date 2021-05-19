    import csv
    import time
    import datetime

    import dt as dt
    import pandas as pd

    with open("/home/dilux/SenzMate/Bogawanthalawa/Analyzing/report.csv", "r", encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['Temp'] > '26.00']

    arr_list = []
    arr_date = []
    for row in rows:
        arr_list.append(row)
        # print(arr_list)
        # print(row)
        # time.sleep(1)
        # print(row['Time'])
        string = row['Time']
        # print(string)

        size = len(string)
        mod_string = string[:size - 3]
        # print(mod_string)

        date_time_obj = datetime.datetime.strptime(mod_string, '%Y-%m-%d %H:%M')
        val = str(date_time_obj.date())
        # print(val)

        # print(val)

        size2 = len(val)
        date_only = val[size2 - 2:]
        date_only = val[size2 - 2:]
        print(date_only)
        #