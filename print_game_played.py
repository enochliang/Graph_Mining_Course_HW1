import json
import math
import numpy as np
import matplotlib.pyplot as plt

data_json = open('data_rank_default.json', encoding="utf-8")

data_txt = data_json.read()

j = json.loads(data_txt)
#print(j[0])

scale = []

for obj in j:
    scale.append(float(obj["league"]["gamesPlayed"]))

arr = np.array(scale)
#print(arr)

plt.subplot(121)
counts,bins,__=plt.hist(arr, bins=np.linspace(arr.min(), arr.max(), 201), rwidth=0.8)
plt.xlabel('x = gamePlayed') 
plt.ylabel('y = number of people')
plt.title("number of people v.s. gamePlayed\nlinear scale")
plt.subplot(122)
new_count = np.array([])
new_bin = np.array([])
for i in range(200):
    if(counts[i]!=0):
        new_count=np.append(new_count,[counts[i]])
        new_bin=np.append(new_bin,[bins[i]])

log_count = np.log(new_count)
log_bins = np.log(new_bin)
#print(log_count)
#plt.hist(arr, bins=np.logspace(np.log10(arr.min()),np.log10(arr.max()),201,base=50.0), rwidth=0.8)
slope, offset=np.polyfit( log_bins, log_count, 1)
plt.scatter(log_bins, log_count)
x = np.linspace(log_bins.min(),log_bins.max(),101)[:-1]
y = x*slope + offset
#plt.scatter(x, y)
plt.plot(x, y, '-',color = "red")
plt.xlabel('log(x)') 
plt.ylabel('log(y)')
plt.text(3,0,f'Gamma = {slope}\nAlpha = {offset}',color = "green")
print(f'Gamma = {slope}')
print(f'Alpha = {offset}')
plt.title("number of people v.s. gamePlayed\nlog-log scale")

#plt.loglog(basex=10,basey=10)
plt.show()

data_json.close()