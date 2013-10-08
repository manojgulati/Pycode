# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt # For plotting functions
import math # No need to import this
import numpy as np #for numerical computations

# <codecell>

x = np.linspace(0,2*3.14,100,True)
y = sin(x)
z = cos(x)
plt.plot(y)
plt.plot(z) # Two functions in same plot

# <codecell>

plt.subplot(2,1,1)
plt.plot(y)
plt.subplot(2,1,2)
plt.plot(z)
plt.ylabel('sin(x)')
plt.show() #Two functions as subplot

# <codecell>


