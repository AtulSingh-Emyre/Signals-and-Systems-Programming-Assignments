import math
import numpy as np
import collections
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#3

#y[n]=sin(2*pi*fa*n*Ts)
x=np.arange(0,11)
fa=75
fs=[40,80,150,300,600]
for i in fs:
    y=np.sin((2*np.pi*fa*x)/i)
    plt.stem(x,y)
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.title('y[n]')
    plt.show()



#LPF with fc=100
x=np.arange(0,18)
y=np.sin(150*np.pi*x/80)
N=16
ak=[]
for k in x:
    s=0
    for n in range(0,N+1):
        s=s+(y[n]*np.exp(-1j*k*n*2*np.pi/N))
    ak.append(s/N)

def lpfil(x):
    if x<=200*np.pi and x>=-200*np.pi:
        return 1
    else:
        return 0


yf=[]
for n in x:
    s=0
    for k in range(0,N+1):
        s=s+(ak[k]*lpfil(np.exp(2*np.pi*k/N))*np.exp(1j*k*2*np.pi*n/N))
    yf.append(s)


plt.plot(x,yf)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('reconstructed signal')
plt.show()


#BPF
def bpfil(x):
    if x<=160*np.pi and x>=120*np.pi:
        return 1
    elif x>=-160*np.pi and x<=-120*np.pi:
        return 1
    else:
        return 0

yf=[]
for n in x:
    s=0
    for k in range(0,N+1):
        s=s+(ak[k]*bpfil(np.exp(2*np.pi*k/N))*np.exp(1j*k*2*np.pi*n/N))
    yf.append(s)


plt.plot(x,yf)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('reconstructed signal')
plt.show()
