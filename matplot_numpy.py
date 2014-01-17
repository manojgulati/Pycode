import numpy as np
#import matplotlib
from pylab import *
import time
#import random
#import pytz
#import matplotlib.use
import matplotlib.pyplot as py

t = np.arange(0,3.14/4, 0.01)
#y = np.cos(3*x)
y=cos(2*t)
Z=sin(2*t);
plt.plot(t, y, marker='o')
plt.plot(t, Z, marker='o')
#plt.xlabel('X')
#plt.ylabel('x*x-6*x+8')
plt.show()