from p2_IO_Status import *
w=get_ws(A,B,C)
up,low=fraction(w)
a1,a2=solve(low, "s")
if a1*a2<0 or (a1>0 and a2>0):
    print("System unstable")
elif a1<0 and a2<0:
    print("System stable")
if abs(a1)==abs(a2) and a1!=0:
    print("System on the border of stability")
