import math
n=int(input("enter the number"))
x=list(range(2,n))
for y in range(2,n):
    for i in range(0,n-2):
        if x[i]%y==0:
            x[i]=0
for i in range(0,n-2):
    if x[i]!=0:
        print (x[i])


        
