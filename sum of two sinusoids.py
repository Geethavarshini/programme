import numpy as np
import matplotlib.pyplot as plt
f1=20
f2=10
fs=500
n=np.arange(0,1000,1)
y1=np.cos(2*(3.14)*f1*n/fs)
y2=np.cos(2*(3.14)*f2*n/fs)
plt.subplot(3,1,1)
plt.plot(n,y1)
plt.subplot(3,1,2)
plt.plot(n,y2)
y=y1+y2
plt.subplot(3,1,3)
plt.plot(n,y)
plt.show()
