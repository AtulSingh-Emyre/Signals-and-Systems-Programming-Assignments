import math
import numpy as np
import collections
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x=np.arange(0,17)
y=[]
for n in x:
    y.append(1+np.sin((3*np.pi*n)/8+np.pi/4))

N=16
ak=[]
for k in x:
    s=0
    for n in range(0,N+1):
        s=s+(y[n]*np.exp(-1j*k*n*2*np.pi/N))
    ak.append(s/N)

def fil(x):
    if x<=-np.pi/3 and x>=-5*np.pi/12:
        return 1
    elif x<=5*np.pi/12 and x>=np.pi/3:
        return 1
    elif x<=-19*np.pi/12 and x>=-5*np.pi/3:
        return 1
    elif x<=5*np.pi/3 and x>=19*np.pi/12:
        return 1
    else:
        return 0

yf=[]
for n in x:
    s=0
    for k in range(0,N+1):
        s=s+ak[k]*fil(np.exp(2*np.pi*k/N))*np.exp(1j*k*2*np.pi*n/N)
    yf.append(s)


yfr=[]
yfimg=[]
for i in yf:
    yfr.append(i.real)
    yfimg.append(i.imag)
plt.stem(x,yfr)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('real part of filtered signal')
plt.show()

plt.stem(x,yfimg)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('imaginary part of filtered signal')
plt.show()

