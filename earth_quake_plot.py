import numpy as np
import matplotlib.pyplot as plt

data_csv = open('earth_quake.csv')

data_lines = data_csv.readlines()[1:-1]

#print(data_lines)

scale = []

for line in data_lines:
    scale.append(float(line.split(',')[-2]))

arr = np.array(scale)
print(arr)

plt.hist(arr,bins=np.linspace(0, 10, 101),rwidth=0.8)
plt.show()

data_csv.close()