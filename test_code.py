
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import csv


x = []
y = []

with open('/home/dilux/SenzMate/Bogawanthalawa/Analyzing/report.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append(int(row[2]))

plt.bar(x, y, color='g', width=0.72, label="Age")
plt.xlabel('Time')
plt.ylabel('Temp')

plt.legend()
# plt.show()
# plt.show()
plt.savefig("mygraph.png")