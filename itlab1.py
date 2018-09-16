#Лабораторная работа № 1

from heapq import *
#use a build-in lab for heapsort(which called pyramidal sort also)

###part1###
def Y_N (answer="non"):
    Y=["Да","да","Yes""YES","Y","y","yes"]
    N=["Нет","нет","не","No","NO","N","n","no"]
    try:
        Y.index(answer)
        return 1
    except:
        try:
            N.index(answer)
            return 0
        except:
            return 2


def task1():
    i=0
    
    q1="Is the country in euroup?"
    
    q2="Is the country largest country?"
    
    q3="Is the country nighbor of the largest country?"
    
    q4="Is the country nearby a sea?"
    
    q5="Is the country in asian?"
    
    q6="Does the country has the best economy?"
    
    q7="Does the country nearby the country which has the best economy?"
    
    q8="Is the country second largest country?"

    q9="Does it has a queen?"

    q10="Dose it has the most people?"

    q=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

    c1= "1011000000Finland"
    c2= "1101000000Russsian"
    c3= "1001000000France"
    c4= "1000000000Switzerland"
    c5= "0011100001China"
    c6= "0011100000North_Korea"
    c7= "0001100000Singapore"
    c8= "0010100000Mongolia"
    c9= "0000000000Sudan"
    c10="0001010000USA"
    c11="0001001100Canada"
    c12="0001001000Mexico"
    c13="1010000000Belarus"
    c14="0001100000United_Arab_Emirates"
    c15="1001000010UK"
    c16="1010000010Hungary"

    Country=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16]
    
    march=Country
    YY=[]
    NN=[]
    uc=""
    pa=[]
    print("###TASK1###")
    print("Select a country from:")
    for c in Country:
        i=i+1
        print(str(i)+"."+c[10:])
    i=-1
    for qq in q:
        i=i+1
        for m in march:
            if m[i]=="1":
                YY.append(m)
            else:
                NN.append(m)
        if len(NN)==0 or len(YY)==0:
            NN=[]
            YY=[]
            print("passed:"+qq+"("+str(len(YY))+"/"+str(len(NN))+")")
            continue
        r=Y_N(input(qq+"("+str(len(YY))+"/"+str(len(NN))+")\nYour Answer:"))
        if r==1:
            march=YY
        elif r==0:
            march=NN
        else:
            print("question passed")
        NN=[]
        YY=[]
        if len(march)==1:
            ans=march[0]
            print("You selected: "+ans[10:])
            break
        elif len(march)==0:
            print("No answer")
            break


            
###part2###
def get_num(part=2):
    numlist=[]
    numlist_part3=[]
    complexlist=[]
    success=0
    strnum=input("Input numbers separated by\",\":\n")
    strnum=strnum.split(",")
    for n in strnum:
        try:
            float(n)
            numlist.append(n)
            numlist_part3.append(float(n))
        except:
            try:
                complexlist.append(complex(n))
            except:
                pass
    if len(complexlist):
        if part==2:
            print("Complex\n"+str(complexlist))
            success=1
    if len(numlist):
        if part==2:
            print("Rational\n"+str(numlist))
            success=1
            return numlist
        else:
            success=1
            return numlist_part3
    if success==0:
        get_num()
    
def is_natural(intlist):
    naturallist=[]
    for n in intlist:
        if int(n)>=0:
            naturallist.append(n)
    if len(naturallist):
        print("Natural\n"+str(naturallist))
        simple(naturallist)

def even_odd(intlist):
    even=[]
    odd=[]
    for n in intlist:
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
    if len(even):
        print("Even\n"+str(even))
    if len(odd):
        print("Odd\n"+str(odd))
        
def simple(naturallist):
    simplelist=[]
    for n in naturallist:
        if n>=1:
            for i in range(2,n):
                if n%i ==0:
                    simplelist.append(n)
                    break
    if len(simplelist):
        print("Simple\n"+str(simplelist))

def is_int(numlist):
    intlist=[]
    for n in numlist:
        if float(n).is_integer():
            intlist.append(int(n))
    if len(intlist):
        print("Integer\n"+str(intlist))
        is_natural(intlist)
        even_odd(intlist)
        

def task2():
    print("###TASK2###")
    numlist=get_num()
    if len(numlist):
        is_int(numlist)



###part3###

def bubblesort(numlist):
    for passnum in range(len(numlist)-1,0,-1):
        for i in range(passnum):
            if numlist[i]>numlist[i+1]:
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp
    print("Bubble Sort")
    print(numlist)
    
def gnomesort(numlist):
    #The Simplest Sort Algorithm
    i,j,size = 1,2,len(numlist)
    while i<size:
        if numlist[i-1]<=numlist[i]:
            i,j = j,j+1
        else:
            numlist[i-1],numlist[i] = numlist[i],numlist[i-1]
            i -= 1
            if i==0:
                i,j = j,j+1
    print("Gnome sort")
    print(numlist)

def blocksort(numlist):
    global nL1
    #print("Splitting ",numlist) alot of splitting...
    if len(numlist)>1:
        mid = len(numlist)//2
        lefthalf = numlist[:mid]
        righthalf = numlist[mid:]

        blocksort(lefthalf)
        blocksort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
            else:
                numlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1
        nL1=numlist
        
def heapsort(numlist):
    h = []
    for n in numlist:
        heappush(h, n)
    return [heappop(h) for i in range(len(h))]

        
def task3():
    print("###TASK3###")
    numlist=get_num(3)
    bubblesort(numlist)
    gnomesort(numlist)
    blocksort(numlist)
    print("Block sort")
    print(nL1)
    print("Pyramidal sort")
    print(heapsort(numlist))

###part4###
def task4():
    print("###TASK3###")
    C=30.0
    D=300
    P_d=D*(1/3.0)*(int(input("In 30 days it happend N times \n N=?:"))/C)
    print("The probability its happend on Карлос is   "+str(P_d))


while 1:
    task1()
    task2()
    task3()
    task4()

