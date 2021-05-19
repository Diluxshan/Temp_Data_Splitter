
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt


plt.plot([1, 2, 3, 4])
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.show()
plt.savefig("mygraph.png")