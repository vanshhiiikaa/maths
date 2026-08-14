#Histogram

import matplotlib.pyplot as plt

s_data = [10,20,30,40,50,60]
plt.hist(s_data)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")

plt.show()