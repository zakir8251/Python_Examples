import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('Python version: ' + sys.version)
print('Numpy version: ' + np.__version__)
print('Pandas version: ' + pd.__version__)

item_list = []
item_arr = np.array(item_list)
print(item_arr)
x=range(0,len(item_arr))
y= item_arr
plt.figure(1)
plt.xlabel("Serial No")
plt.ylabel("Slope (db10/degC)")
plt.legend()
plt.plot(x,y, label='Slope')

plt.figure(2)
plt.xlabel("Serial No")
plt.ylabel("Slope (db10/degC)")
plt.scatter(x,y)

plt.figure(3)
plt.xlabel("Slope (db10/degC)")
plt.xlabel("Frequency")
plt.hist(y)

plt.show()
