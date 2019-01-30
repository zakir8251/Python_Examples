import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

print('Python version: ' + sys.version)
print('Numpy version : ' + np.__version__)
print('Pandas version: ' + pd.__version__)

x = np.arange(0, 1*np.pi, 0.1)
y1 = x
y2 = x*np.log(x)
y3 = np.log(x)

fig=plt.figure(1, figsize=(15,7))
ax = fig.add_subplot(111)
plt.xlabel('n', fontsize=18)
plt.ylabel('f(n)', fontsize=18)

ax.plot(x,y1)
ax.plot(x,y2)
ax.plot(x,y3)
ax.plot(x,x*x)

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.legend(['n', 'log(n)','nlog(n)', 'n^2'], loc='upper center', fontsize=18)
plt.show()
