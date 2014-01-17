import numpy as np
#import matplotlib
from pylab import *
import time
import random
import pytz
#import matplotlib.use
import matplotlib.pyplot as py


X_size=100
Y_size=100
predecimal_range=[20,25]
postdecimal_range=[0,1000]
#X = np.linspace(-np.pi, np.pi,256, endpoint=True)
#X = np.linspace(np.pi/2, 2*np.pi,256, endpoint=True)
#C, S = np.cos(X), np.sin(X)
X=[0]*X_size
Y=[0]*Y_size
Z=[0]*X_size
P=[0]*X_size
Q=[0]*X_size
R=[0]*X_size
number_of_elements=0
threshold=2
current_timestamp=int(time.time())

for i in range(0,X_size):
	X[i]=current_timestamp+i
	Y[i]=float(random.randint(20,25))+float(random.randint(0,1000))/1000
	Z[i]=datetime.datetime.fromtimestamp(X[i],pytz.timezone('Asia/Kolkata'))
	if 	Y[i]-Y[i-1]>1:
		P[i]=Y[i]-Y[i-1]
		Q[i]=((Q[i]*i)+Y[i])/(i+1)
		#number_of_elements=number_of_elements+1
	
		#simple moving avg
		R[i]=(Y[i]+Y[i-1]+Y[i-2]+Y[i-3]+Y[i-4])/5			

#subplot(411)
py.plot(Z,Y)
#subplot(412)
#py.plot(Z,P)
#subplot(413)
#py.plot(Z,Q)
#subplot(414)
py.plot(Z,R)

#figure=py.gcf()
#figure.autofmt_xdate()
#py.plot(Z,Y)

py.show()