import math
import matplotlib.pyplot as plt
print("Task 1 var 9")
print("u=9cos(4t)")
while 1:
    try:
        a=float(input("a=?\n"))
        b=float(input("b=?\n"))
        break
    except:
        pass
t=0
dt=0.01
y=0
tl=[]
yl=[]
while t<=10:
    tl.append(t)
    yl.append(y)
    u=9*(math.cos(4*t))
    y=0.5*((b*u-y*a)+y)*dt
    t=t+dt
plt.plot(tl,yl)
plt.show()
