import numpy as np
import time

a = [[0, -1, 3, 5], [2, -7, 2, 6], [0, 4, -6, 6], [2, 0, 0, -2]]
b = [[0], [2], [6], [4]]
c = [[0, -1, 3, 5]]
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

def controllability(A, B):   
    A = np.asmatrix(A)
    B = np.asmatrix(B)
    n = A.shape[0]
    m = B.shape[1]
    E = np.asmatrix(np.zeros((n, n*m)))
    x = B
    for i in range(0, n):
        j = i * m
        E[:n, j:j+m] = x
        x = A * x
    print(E)
    if get_rank(E.tolist())==E.shape[0]:
        isctr=True
    else:
        isctr=False
    return isctr

def controllability_numpy(A, B):
    A = np.asmatrix(A)
    B = np.asmatrix(B)
    n = A.shape[0]
    C=B
    for i in range(1, n):
        C = np.hstack((C, A**i*B))
    print(C)
    if np.linalg.matrix_rank(C)==C.shape[0]:
        isctr=True
    else:
        isctr=False
    return isctr
    
def observability(A, C):
    A = np.asmatrix(A)
    C = np.asmatrix(C)
    n = A.shape[0]
    q = C.shape[0]
    O = np.asmatrix(np.zeros((n*q, n)))
    y = C
    for i in range(0, n):
        j = i * q
        O[j:j+q, :n] = y
        y = y * A
    if get_rank(O.tolist())==O.shape[0]:
        isobs=True
    else:
        isobs=False
    print(O)
    return isobs

def observability_numpy(A, C):
    A = np.asmatrix(A)
    C = np.asmatrix(C)
    n = A.shape[0]
    O = C
    for i in range(1, n):
        O = np.vstack((O, C*A**i))
    print(O)
    if np.linalg.matrix_rank(O)==O.shape[0]:
        isobs=True
    else:
        isobs=False
    return isobs

print("A:")
print(np.asmatrix(a))
print("B:")
print(np.asmatrix(b))
print("C:")
print(np.asmatrix(c))
print("rank:")
s=time.time()
print(get_rank(a))
e=time.time()
print("Time used:"+str(e-s))
print("rank(numpy):")
s=time.time()
print(np.linalg.matrix_rank(a))
e=time.time()
print("Time used:"+str(e-s))
print("Is controllable:")
s=time.time()
print(controllability_numpy(a, b))
e=time.time()
print("Time used:"+str(e-s))
print("Is controllable(numpy):")
s=time.time()
print(controllability(a, b))
e=time.time()
print("Time used:"+str(e-s))
print("Is observabble:")
s=time.time()
print(observability(a, c))
e=time.time()
print("Time used:"+str(e-s))
print("Is observabble(numpy):")
s=time.time()
print(observability_numpy(a, c))
e=time.time()
print("Time used:"+str(e-s))
