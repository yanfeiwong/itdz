import matplotlib.pyplot as plt
import random

#Part 1
randlist=[]
for i in range(50):
    n=random.randint(0,40)
    randlist.append(n)
print("Got random list: "+str(randlist))
plt.plot(randlist,label='Original data')

def Moving_average(lis,level=3):
    n=0
    malist=[]
    ma2list=[]
    for i in range(len(lis)):
        try:
            for ii in range(i,i+(int(level)-1)):
                n=n+lis[ii]
            n=n/float(level)
            malist.append(n)
            ma2list.append((i*2+(int(level)-1))/2)
            n=0
        except:
            pass
    plt.plot(ma2list,malist,label='Moving average (Filter width:'+str(level)+')')


def Savitzky_Golay(lis):
    n=0
    sglist=[]
    sg2list=[]
    for i in range(len(lis)):
        if i>=2:
            try:
                n=(1/35.0)*(-3*lis[i-2]+12*lis[i-1]+17*lis[i]+12*lis[i+1]-3*lis[i+2])
                sglist.append(n)
                sg2list.append(i)
            except:
                pass
        else:
            pass
    plt.plot(sg2list,sglist,label='Savitzky Golay (Filter width:5)')
    
def First_order_filter(lis,a):
    n=0
    n0=lis[0]
    folist=[]
    for i in range(len(lis)):
        n=a*lis[i]+(1-a)*n0
        folist.append(n)
        n0=n
    plt.plot(folist,label='First order filter (a='+str(a)+')')    

def Median_filter(lis,level=5):
    n=0
    mflist=[]
    for i in range(len(lis)):
            m0=[]

            try:
                for ii in range(i-int(level/2),i+int(level/2)+1):
                    m0.append(lis[ii])
                m0.sort()
                n=m0[int(level/2)]
                mflist.append(n)
            except:
                pass
    plt.plot(mflist,label='Median_filter (Filter width:'+str(level)+')')
        
        

Moving_average(randlist,level=5)
Savitzky_Golay(randlist)
First_order_filter(randlist,0.1)
Median_filter(randlist,level=7)
plt.legend(loc='upper right')
plt.show()
