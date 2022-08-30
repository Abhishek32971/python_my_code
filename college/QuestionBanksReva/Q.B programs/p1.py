counte=0
counto=0
sume=0
sumo=0
while True:
    x=input("enter a number\n")
    if x=="done":
        break
    x=int(x)
    if x%2==0 :
        counte+=1
        sume+=x
    else:
        counto+=1
        sumo+=x
print("sum of even is %d and the sum of odd is %d"%(sume,sumo))
print("count of even is %d and sum of odd is %d"%(counte,counto))