'''consider a program that adds a maximum of 10 odd numbers'''
sum0=0
c=0
while True:
    x=int(input("enter a number "))
    if(x%2==0):
        continue
    else:
        sum0+=x
        c+=1
    if (c==10):
        break
    print(c)
print("the sum is",sum0)

    