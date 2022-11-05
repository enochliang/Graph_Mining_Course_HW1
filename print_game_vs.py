import json
import numpy as np
import matplotlib.pyplot as plt

data_json = open('data_rank_default.json', encoding="utf-8")

data_txt = data_json.read()

j = json.loads(data_txt)
print(j[0])

scale = []

for obj in j:
    scale.append(float(obj["league"]["vs"]))

arr = np.array(scale)
print(arr)

plt.subplot(121)
_,bins,__=plt.hist(arr, bins=np.linspace(arr.min(), arr.max(), 201), rwidth=0.8)
plt.subplot(122)
print(bins)
#plt.hist(arr, bins=np.logspace(np.log10(arr.min()),np.log10(arr.max()),201,base=50.0), rwidth=0.8)
plt.hist(arr, bins=np.linspace(arr.min(), arr.max(), 201), rwidth=0.8)
plt.xscale('log')
plt.yscale('log')
plt.show()

data_json.close()