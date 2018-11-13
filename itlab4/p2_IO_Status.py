from sympy import *

A=[[-7,0,0],[0,-5,0],[0,0,-1]]
B=[[7],[2],[1]]
C=[[1,2,0]]
#Ones
def ones(s):
    e=[]
    for i in range(s):
        e0=[]
        for ii in range(s):
            if ii==i:
                e0.append(1)
            else:
                e0.append(0)
        e.append(e0)
    return e
            
            
#Matrix multiplication
def mat_mu(A,B):
    ans=[]
    s1=len(A)
    s2=len(A[0])
    s4=len(B[0])
    for i in range(s1):
        ans_l=[]
        for jj in range(s4):
            a=0
            for j in range(s2):
                a=a+A[i][j]*B[j][jj]
            ans_l.append(a)
        ans.append(ans_l)
    return ans

#Inverse matrix 3x3
def mat_3x3_ob(A):
    a=A[0][0]
    b=A[0][1]
    c=A[0][2]
    d=A[1][0]
    e=A[1][1]
    f=A[1][2]
    g=A[2][0]
    h=A[2][1]
    i=A[2][2]
    aaa=(a*e*i+b*f*g+c*d*h)-(c*e*g+f*h*a+i*b*d)
    aaa=1/(aaa)
    ans=[[(aaa*(e*i-h*f)),((-aaa)*(b*i-h*c)),(aaa*(b*f-c*e))],[(aaa*(f*g-i*d)),((-aaa)*(c*g-i*a)),(aaa*(c*d-a*f))],[(aaa*(d*h-g*e)),((-aaa)*(a*h-g*b)),(aaa*(a*e-b*d))]]
    return ans

#Rank
def swapRows(A,row1,row2):
    A[row1],A[row2]=A[row2],A[row1]
    return(A)
def swapColumns(A,column1):
    for i in range(len(A[0])):
	    A[i][0],A[i][-1]=A[i][-1],A[i][0]
    return(A)
def Row_Transformation(A,x,row1,row2):
    for i in range(len(A[row2])):
	    A[row2][i]=A[row2][i]-x*A[row1][i]
    return(A)
def get_rank(A):
    rank=min(len(A[0]),len(A))
    for row in range(0,rank):
	    if A[row][row]!=0 and len(A)>len(A[0]):
		    for cnt in range(row+1,rank+len(A)-len(A[0])):
			    oper=A[cnt][row]/A[row][row]
			    Row_Transformation(A,oper,row,cnt)
	    elif A[row][row]!=0 and len(A[0])>=len(A):
		    for cnt in range(row+1,rank):
			    oper=A[cnt][row]/A[row][row]
			    Row_Transformation(A,oper,row,cnt) 

	    else:
		    for cnt in range(row+1,rank):
			    if A[row][cnt]==0:
				    swapRows(A,row,cnt)
			    else:
				    swapColumns(A,cnt)
    cnt=0
    for n in range(len(A)):
	    if A[n]!=[0.0]*(len(A[0])):
		    cnt+=1
    return(cnt)

#W(s)
def get_ws(A,B,C):
    s=symbols('s')
    temp=[[s-A[0][0],-A[0][1],-A[0][2]],[-A[1][0],s-A[1][1],-A[1][2]],[-A[1][0],-A[2][1],s-A[2][2]]]
    temp=mat_3x3_ob(temp)
    temp=mat_mu(C,temp)
    temp=mat_mu(temp,B)
    temp=simplify(temp[0][0])
    return temp

#Controllability
def ctr(A,B):
    s=len(A)
    y=[]
    for n in range(s):
        e=ones(s)
        for nn in range(n):
            e=mat_mu(e,A)
        aa=mat_mu(e,B)
        y.append(aa)
    s2=len(y)
    s3=len(y[0])
    t=[]
    for i in range(s3):
        l=[]
        for ii in range(s2):
            l.append(y[ii][i][0])
        t.append(l)
    y=t
    if get_rank(y)==s2:
        return "Controllable"
    else:
        return "Uncontrollable"
#Observability
def obv(A,C):
    s=len(A)
    y=[]
    for n in range(s):
        e=ones(s)
        for nn in range(n):
            e=mat_mu(e,A)
        aa=mat_mu(C,e)
        y.extend(aa)
    s2=len(y)
    s3=len(y[0])
    t=[]
    for i in range(s3):
        l=[]
        for ii in range(s2):
            l.append(y[ii][i])
        t.append(l)
    y=t
    if get_rank(y)==s2:
        return "Observable"
    else:
        return "Unobservable"

if __name__ == '__main__':
    print("A=",A)
    print("B=",B)
    print("C=",C)
    print("W(s)=",get_ws(A,B,C))
    print("System:",ctr(A,B),",",obv(A,C))
        
            
    
