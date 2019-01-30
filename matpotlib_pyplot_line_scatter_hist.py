import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

print('Python version: ' + sys.version)
print('Numpy version : ' + np.__version__)
print('Pandas version: ' + pd.__version__)

item_list = [1,2,0.5,3]
item_arr = np.array(item_list)
print(item_arr)
x=range(0,len(item_arr))
y= item_arr
plt.figure(1, figsize=(15,7))
plt.xlabel("Serial No", fontsize=18)
plt.ylabel("Items", fontsize=18)
plt.plot(x,y, label='Slope')
plt.legend(fontsize=18)

plt.figure(2, figsize=(15,7))
plt.xlabel("Serial No", fontsize=18)
plt.ylabel("Items", fontsize=18)
plt.scatter(x,y)

plt.figure(3, figsize=(15,7))
plt.xlabel("Items", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.hist(y)

plt.show()
