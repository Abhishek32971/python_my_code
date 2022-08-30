import numpy as np
'''#0d array
x=np.array(43)
print(x)
#1d array
ar=np.array([1,2,3])
print(ar)
print(ar[0])
#traceback if you give more than needed dimensions
#print(ar[0,0])

#2d array
ar=np.array([[1,2,3],[2,3,4]])
print(ar)
print(ar[-1,-1])
ar=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(ar)
print(ar[2,2])

#4d array
ar=np.array([1,2,3],ndmin=4)
print(ar.ndim)

arr = np.array([2,4,6,8,10,12,14,16])
print(arr[3:6])  # will print the elements from 3 to 5
print(arr[:5])  # will print the elements from 0 to 4
print(arr[2:])  # will print the elements from 2 to length of the array.
print(arr[-5:-1])  # will print from the end i.e. -5 to -2
print(arr[:-1])  # will print from end i.e. 0 to -2

#shape and reshape
arr=np.array([1,2,3])
print(arr.shape)
#arr.shape=(2)
print(arr)

arr=np.arange(1,11)
newarr=arr.reshape(5,2)
print(newarr)

#transpose
m1=np.array([[1,2,3],[2,3,4],[4,5,6]])
m2=np.array([[2,3,4],[5,6,7],[7,8,8]])
m3=m1+m2
m4=m1-m2
print(m3)
print(m4)
print(m1)
m5=np.transpose(m1)
print(m5)

print(m2)
m6=m2.transpose()
print(m6)
print(m6[1,])

m1[1][1]=5
print (m1)

def read(m,n,matrix):
    for i in range(m):
        for j in range(n):
            matrix[i][j]=int(input("enter value"))
m=int(input("enter the size of rows"))
n=int(input("enter the size of column))"))
print("enter the values into the input now ")
matrix=np.ndarray(shape=(m,n),dtype=int)
read(m,n,matrix)
print(matrix)
x=int(input("enter the row u want to see"))
print(matrix[x])
y=int(input("enter the column you want to see"))
print(matrix[:,y])

'''