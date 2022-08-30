
n=int(input("enter the number until which you want to print"))

n1,n2=0,1
count=0


if n==1:
    print(0,"end of series")


else:
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    print("end of series")
