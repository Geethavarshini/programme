import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,100,1)
def z(a,w,s):
 x=a*np.cos(w*t+s)
 return x
x1=z(5,50,0)
x2=z(10,50,0)
x=x1+x2
plt.subplot(3,1,1)
plt.plot(t,x)
y1=z(5,50,0)
y2=z(5,100,0)
y=y1+y2
plt.subplot(3,1,2)
plt.plot(t,y)
a1=z(5,50,90)
a2=z(5,50,-90)
a=a1+a2
plt.subplot(3,1,3)
plt.plot(t,a)
plt.show()
