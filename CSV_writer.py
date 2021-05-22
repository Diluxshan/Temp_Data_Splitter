import csv
import time
import datetime

import dt as dt
import pandas as pd

with open("/home/dilux/SenzMate/Bogawanthalawa/Analyzing/may_21.csv", "r", encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader if row['Temp'] > '26.00']

arr_list = []
arr_date = []
arr_month_date = []

for row in rows:
    arr_list.append(row)
print(arr_list)

with open("/home/dilux/SenzMate/Bogawanthalawa/Analyzing/output_may21.csv","w",newline="") as f:
    title = "Time,Temp".split(",") # quick hack
    cw = csv.DictWriter(f,title,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    cw.writeheader()
    cw.writerows(arr_list)
    #