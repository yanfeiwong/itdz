import math
import matplotlib.pyplot as plt

#For: 6y(1)+y=5u

k=5
t=6

w=-10
wl=[]
al=[]
fl=[]
while w<=10:
    a=k/(math.sqrt(1+t*t*w*w))
    f=-math.atan(t*w)
    al.append(a)
    fl.append(f)
    wl.append(w)
    w=w+0.01
plt.plot(wl,al,label="АЧХ")
plt.plot(wl,fl,label="ФЧХ")
plt.legend(loc='upper right')
plt.show()
