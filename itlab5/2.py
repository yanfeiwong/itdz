############################
#Task 2 var 9
############################
#A(B)
#Линейная система
#A=0.5B
############################
#B(C)
#Любой тип системы (Нелинейная)
#B=tg(C)
############################
#C(A)
#Статическая система
#C=arctg(2A)
############################
import xlwt,os,math
import matplotlib.pyplot as plt
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('Task2', cell_overwrite_ok=True)
l=0
i=-10
i1=0
i2=0
il=[]
ill=[]
illl=[]
while i<=10:
    sheet.write(l, 0, i)
    i1=2*i
    ill.append(i1)
    sheet.write(l, 1, i1)
    i2=math.atan(i)
    illl.append(i2)
    sheet.write(l, 2, i2)
    i=i+0.1
    il.append(i)
    l=l+1
book.save(r'task2.xls')
os.system(r'task2.xls')
plt.plot(ill,il,label='A(B) Линейная')
plt.plot(illl,ill,label='B(C) Нелинейная')
plt.plot(il,illl,label='C(A) Статическая')
plt.legend(loc='upper right')
plt.show()


