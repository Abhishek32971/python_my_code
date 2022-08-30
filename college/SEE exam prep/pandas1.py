import pandas as pd
a=[1,2,3]
x=pd.Series(a)
print(a)
print(a[0])


#indexing
x=pd.Series(a,index=["a",'b','c'])
print(x)
print(x["a"])

#dictionary
y={"a":123,"b":345,"c":567}
x=pd.Series(y,index=["a","b"])
print(x)

x["a"]=20
print(x)

