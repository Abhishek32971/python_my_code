'''
str1="everything is lost"
print(str1[1:40])


def slicing():
	m=int(input("Enter the starting index value or index1"))
	n=int(input("Enter the ending index value or index2"))
	substr=str1[m:n]
	print("String extracted between index1 and index2 is",substr)
str1=str(input("Enter the string"))
slicing()
del str1

str1="everything ise loest"
s=str1.split('e',3)
print(s)



str1=("8888")
if str1.isdigit():
    print("yupp")
if str1.find("r"):
    print("yes")


a=4
b="abadaba"
c=5.6

print("this %d is number   \n this %s is string \n this is float %f"%(a,b,c))
print(f"this {a} is number \n this {b}is string \n this {c} is float ")
print("this is {} this is {} this is {}".format(a,b,c))
'''
b="isabela"
print(b[::2])
print(b[::-2])
print(b[-1:4])
print(b.strip("i"))
print(b.index("i"))

x="lambda"
x+=x
print(x)

str1='REVA'
str1=str1.center(10)
print(str1)
