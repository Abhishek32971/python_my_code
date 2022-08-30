x=input("enter the sentance\n")
y=x.split()
n=len(y)
z=len(y[0])
u=y[0]
for i in range(n):
    if len(y[i])>z:
        z=len(y[i])
        u=y[i]
print("the longest in the list is",u)