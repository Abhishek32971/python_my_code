'''txt = 'but soft what light in yonder window breaks'
words = txt.split()
print("words:",words)
t = list()
for word in words:
    t.append((len(word), word))
print("t",t)
print(type(t[1]))
t.sort(reverse=True)
print(t)
res = list()
for length, word in t:
    res.append(word)
    print("individual res",res)

print("final res:",res)'''
'''from xml.etree.ElementTree import PI'''


'''x = "Python is "
y = "awesome"
z =  x + y
print(z)
print()'''
'''x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
'''
'''import math
a=float(input("Enter side1"))
b=float(input("Enter side2"))
c=float(input("Enter side3"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of Triangle=", area)
'''
'''a=int(input("Enter first value"))
b=int(input("Enter second value"))
print("Before swapping, value of a=", a)
print("Before swapping, value of b=", b)
a,b=b,a
print("After swapping, value of a=", a)
print("After swapping, value of b=", b)'''



'''def myfunction (country="india"):
    print("my favourite country is "+country)
myfunction ("usa")
myfunction()'''

'''L1 = ["apple", "banana", "cherry"]
print(L1 [-1:-2])'''


'''L1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(L1[-4:-1])'''
'''L1.insert(2,"index2")
print(L1)
L1 = ["apple", "banana", "cherry"]
L1.pop(1)
print(L1)
print(L1.count("apple"))
S1 = {"apple", "banana", "cherry"}
print("banana" in S1)

print(7//3)'''


'''str1='CSE'
str2='ECE'
if str1 > str2:
    print('str1 is greater than str2')
elif str1 < str2:
    print('str2 is greater than str1')
else:
    print('str1 is equal to str2')'''
   
'''
def brin(a,b):
    c=a[b]
    return c
a=input("enter the string")
b=int(input("enter the index"))
d=brin(a,b)
print("the string is ",a)
print("the string character at index is ",d)'''

'''s="hello"
print(s[])'''

'''strin="10 20"
x=strin.split()
#x=int(x)
print(type(x[1]))
for i in x:
    i=int(i)
    print(type(i))'''

'''typle1=([10,20,30],"reva",[5,15,9],(40,50))
print(typle1[3])
t=list(typle1[3])
print(t[1])
'''

'''t={1:2,3:4}
t2=dict
print(t2.copy(t))
print(t2)
'''
print("big"<"small")