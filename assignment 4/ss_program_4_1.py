import math
import numpy as np
import collections
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#1
#unilateral z transform
#x[n]=(1/2)^n
#after doing calculation we find that X(z)=2z/(2z-1) with ROC |z|>1/2

fig, ax = plt.subplots()
ax.set(xlim=(-1, 1), ylim = (-1, 1))
a_circle = plt.Circle((0, 0), .5,label='Not in ROC')
ax.add_artist(a_circle)
patches = [mpatches.Patch(color="blue", label="Not in ROC")]
plt.legend(handles=patches)


x=np.arange(0,11)
def unitstep(x):
    if x>=0:
        return 1
    else:
        return 0

def prev(x,y):
    if x<0:
        return 2
    else:
        return y[n-1]

#the corresponding recursive equation is 2y[n]+y[n-1]=x[n]
y=[]
for n in x:
    y.append((math.pow(1/4,n)*unitstep(n)-prev(n-1,y))/2)


plt.stem(x,y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('y[n]')
plt.show()

