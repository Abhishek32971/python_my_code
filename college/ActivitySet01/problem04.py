hrs = input("Enter Hours:")
h = float(hrs)
rate=float(input("enter rate:"))

if h>40 :
    final1=40*rate + (h-40)*(rate*1.5)
else :
    final1=h*rate
print(final1)