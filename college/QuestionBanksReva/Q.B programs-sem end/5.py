def input1(n):
    dict1=dict()
   
    for i in range(n):
        x=input("enter orprator operand operand")
        x=x.split()
        dict1[x[0]]=x[1:3]
    return dict1



n=int(input("enter the number of items in dict"))
dict2=input1(n)
