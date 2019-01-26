import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,100,1)
def z(a,w,s):
 m=a*np.cos(w*t+s)
 return m
a1=5
a2=10
w1=50
w2=100
s1=45
s2=90
x1=z(a1,w1,s1)
x2=z(a1,w2,s1)
x3=z(a1,w1,s2)
x4=z(a1,w2,s2)
x=x1+x2+x3+x4
plt.subplot(3,1,1)
plt.plot(t,x)
y1=z(a1,w1,s1)
y2=z(a2,w1,s2)
y3=z(a1,w1,s2)
y4=z(a2,w1,s1)
y=y1+y2+y3+y4
plt.subplot(3,1,2)
plt.plot(t,y)
c1=z(a1,w1,s1)
c2=z(a1,w2,s1)
c3=z(a2,w1,s1)
c4=z(a2,w2,s1)
c=c1+c2+c3+c4
plt.subplot(3,1,3)
plt.plot(t,c)
plt.show()
