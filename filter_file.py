import pandas as pd
import csv
import time

df = pd.read_csv('/home/dilux/SenzMate/Bogawanthalawa/Analyzing/report.csv')
temp = df[['Temp']] #select the temp column
#print(temp)
