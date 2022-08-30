def computepay(hrs,rate):
    if (hrs>40):
    	f=40*rate + (hrs-40)*(1.5*rate)
    else :
    	f=rate*hrs
    return f

hrs = input("Enter Hours:")
hrs=float(hrs)
rate=input("enter rate:")
rate=float(rate)
p = computepay(hrs,rate)
print("Pay", p)