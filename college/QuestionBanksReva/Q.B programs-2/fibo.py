from re import A


def fibo():
    a=0
    b=1
    while(True):
        yield a
        a,b=b,a+b
 
for i in fibo():
    print (i)