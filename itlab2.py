import gspread,math,random,os
import matplotlib.pyplot as plt
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
var=9.0

#set up google sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('LabWork-a0efb24d4150.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Lab2").sheet1

print("###Part1###\n var=9")
while 1:
    minn=input("Input range Min: ")
    try:
        minn=float(minn)
        break
    except:
        pass
while 1:
    maxx=input("Input range Max: ")
    try:
        maxx=float(maxx)
        break
    except:
        pass   

rowx=[]
rowy=[]
n=math.ceil(math.sqrt(var)*10)

for i in range(n):
    while 1:
        nn=random.uniform(minn,maxx)
        try:
            rowx.index(nn)
        except:
            rowx.append(nn)
            break
      
for i in range(n):
    while 1:
        nn=random.uniform(minn,maxx)
        try:
            rowy.index(nn)
        except:
            rowy.append(nn)
            break
        


sumx=sum(rowx)
x2=map(lambda x:x*x,rowx)
sumx2=sum(list(x2))

sumy=sum(rowy)
y2=map(lambda y:y*y,rowy)
sumy2=sum(list(y2))

xy=map(lambda x,y:x*y,rowx,rowy)
sumxy=sum(list(xy))

a=(n*sumxy-sumx*sumy)/(n*sumx2-sumx*sumx)
b=(sumy-a*sumx)/n

print("x="+"\n"+str(rowx)+"\ny=\n"+str(rowy)+"\n\ny="+str(a)+"*x+"+str(b))

plt.plot([minn,maxx],[(minn*a+b),(maxx*a+b)])
plt.scatter(rowx,rowy)

sheet.delete_row(1)
sheet.delete_row(1)
sheet.insert_row(rowx,1)
sheet.insert_row(rowy,2)

os.system(
    '"C:/Program Files/Internet Explorer/iexplore.exe"https://docs.google.com/spreadsheets/d/1JIFr-4E1RUN26jZ0Z6PdsXG6RTNN3LpA2tQo8gADBFo/edit?usp=sharing')

print("\nData saved\nPart1 Down")
print("Close the matplotlib window to continue")
plt.show()

print("###Part2###")


def save_mat(n,r,mat):
    mat=np.array(mat,dtype=float) # ro you will get a int32 error ==...
    sheet = client.open("Lab2").get_worksheet(n-1)
    for i in range(r):
        sheet.delete_row(1)
    for i in range(r):
        sheet.insert_row(list(mat[i]),(i+1))


nn=np.random.randint(0,30,size=[n,n])#n*n random numbers from 0 to 30
#about to get 10 iteam to delet
missi=[]
missj=[]
for i in range(10):
    while 1:
        x=random.randint(0,n-1)
        try:
            missi.index(x)
        except:
            missi.append(x)
            break
      
for i in range(10):
    while 1:
        x=random.randint(0,n-1)
        try:
            missj.index(x)
        except:
            missj.append(x)
            break
nfd=nn.copy()#nn after 'deleted' 10 item
missing=list(map(lambda x,y:[x,y],missi,missj))
for i in missing:
        nfd[i[0],i[1]]= 999
        

print(nn)
print(nfd)
#save_mat(2,n,nn)
#save_mat(3,n,nfd)

###Метод Винзорирования###
X_vin = np.copy(nfd)
for i in np.arange(X_vin.shape[0]):
    for j in np.arange(X_vin.shape[1]):
        if X_vin[i,j] == 999:
            if j==0 and X_vin[i,j+1]!=999:
                X_vin[i,j]=X_vin[i,j+1]
            elif X_vin[i,j-1] != 999:
                X_vin[i,j]=X_vin[i,j-1]
            elif j<=(n-2)and X_vin[i,j+1] != 999:
                X_vin[i,j]=X_vin[i,j+1]
            else:
                X_vin[i,j]=random.randint(0,30)
print(X_vin)
#save_mat(4,n,X_vin)
###Метод линейной аппроксимации###          
X_lin = np.copy(nfd)
list_i=[]
for i in range (n-1):# n item in a line , but we do need only need n-1 , missing value is out
    i=i+1
    list_i.append(i)
for i in np.arange(X_lin.shape[0]):
    i_cheak=0
    for j in np.arange(X_lin.shape[1]):
        if X_lin[i,j] == 999:
            temp_line=list(X_lin[i])
            del temp_line[j]
            if i_cheak==0:
                sumx=sum(list_i)
                x2=map(lambda x:x*x,list_i)
                sumx2=sum(list(x2))
                sumy=sum(X_lin[i])
                y2=map(lambda y:y*y,temp_line)
                sumy2=sum(list(y2))
                xy=map(lambda x,y:x*y,list_i,temp_line)
                sumxy=sum(list(xy))
                a=(n*sumxy-sumx*sumy)/(n*sumx2-sumx*sumx)
                b=(sumy-a*sumx)/n
                X_lin[i,j]=a*j+b
            else:
                 X_lin[i,j]=a*j+b #case we have a,b already
            
print(X_lin)
#save_mat(5,n,X_lin)
###Метод корреляционного восстановления ###
X_corr = np.copy(nfd)
while 1:
    try:
        fix_i=int(input("You want to fix line(1,2,3....):"))-1
        fix=X_corr[fix_i]
        print("Fixing line "+str(fix_i))
        print(fix)
    except:
        fix=X_corr[1]
        print("Fixing line 2")
        print(fix)
    try:
        use_i=int(input("You want to use line(1,2,3....):"))-1
        use=X_corr[use_i]
        print("Using line "+str(use_i))
        print(use)
    except:
        use=X_corr[0]
        print("Using line 1")
        print(use)
    i=-1
    for j in fix:
        i=i+1
        if j==999:
            X_corr[fix_i,i]=use[i]
    try:
        cc=int(input("Input 1 to continue:"))
        if cc!=1:
            break
    except:
        break
print(X_corr)
#save_mat(6,n,X_corr)
print("Part2 Down\n\n\n\n")



print("###Part3###")
#matrix nn is not changed , we can still use it
i=0
for l in range(n):
    i=i+1
    me=sum(nn[(i-1)])/n
    print("Line"+str(i)+"  Mathematical Expectation: "+str(me)+"  Dspersion: "
          +str(sum(list(map(lambda x:x*x,nn[(i-1)])))/n-(me**2)))
list_i=[]
for i in range (n):
    i=i+1
    list_i.append(i)
np.warnings.filterwarnings('ignore')
def erroline(line,maxerro):
    l=nn[line]
    l2=list_i
    a=(n*(sum(list(map(lambda x,y:x*y,l2,l))))-sum(l)*sum(l2))/(
        n*sum(list(map(lambda x:x*x,l2)))-sum(l2)**2)
    b=(sum(l)-a*sum(l2))/n
    if a==0:
        return False
    for i in range(n):
        if l2[i]!=0:
            relErro=abs(((a*l2[i]+b)-l[i])/(a*l2[i]+b))
        else:
            relErro=abs(l[i])
    if relErro < maxerro:
        print("Line"+str(line+1)+": linear relationship    e="+str(relErro))

def erroexp(line,maxerro):
    l=nn[line]
    l2=list_i
    a=np.exp(sum(list(map(lambda x,y:(np.log(y)-x),l2,l)))/n)
    for i in range(n):
        if l2[i]==0:
            continue
        relErro=abs((a*np.exp(l2[i])-l[i])/(a*np.exp(l2[i])))
        if relErro>maxerro:
            return False
    print("Line"+str(line+1)+": exponential relationship    e="+str(relErro))
maxerro=float(input("Input MaxError:"))        
for l in range(n):
    erroline(l,maxerro)
    erroexp(l,maxerro)
###All done###
