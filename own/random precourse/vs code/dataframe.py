#creating empty dataframe
'''import pandas as pd
df=pd.DataFrame[]
print(df)'''

#creat df using series
'''import pandas as pd
import numpy as np
arr=np.arange(5,26,5)
print(arr)
S=pd.series(arr)
print(S)
df=pd.DataFrame(S)
print(df)'''

# createdf using dictionary
'''import pandas as pd
name=pd.Series(['ram','sham'])
city=pd.Series(['bang','mys'])
D={'name':name,'city':city}
df=pd.DataFrame(D)
print(df)'''

#create df of a student report card



#create df using list of dictionary
'''import pandas as pd
L=[{'name':'charan','marks':83},{'name':'ran','marks':80},{'name':'cha','marks':88},{'name':'aran','marks':87}
df=pd.DataFrame(L)
print(df)'''

#iteration of  dataframe


#iter rows()
'''import pandas as pd
L=[{'name':'charan','marks':83},{'name':'ran','marks':80},{'name':'cha','marks':88},{'name':'aran','marks':87}]
df=pd.DataFrame(L)
print(df)
for(row_index,rows_value) in df.iterrows():
   print('\n row index is::',row_index)
   print('row value is::')
   print(rows_value)'''

#iteritems()

'''import pandas as pd
L=[{'name':'charan','marks':83},{'name':'ran','marks':80},{'name':'cha','marks':88},{'name':'aran','marks':87}]
df=pd.DataFrame(L)
print(df)
for(col_name,col_value) in df.iteritems():
   print('\n column name is::',col_name)
   print('column values::')
   print(col_value)'''

#selection on df

'''import pandas as pd
empdata={'empid':[10,11,12,13,14,15],
         'ename':['sachin','bandaru','gunda','vijay','arun','varun'],
         'doj':['12-01-2013','12-01-2014','12-01-2015','12-01-2016','12-01-2017','12-01-2019']}
df=pd.DataFrame(empdata)
print(df)
print(df.empid)
print(df['empid'])
print(df[['empid','ename']])#instead of l=[jdfj,wfdjf] we use[[kdjjde,ahdjadje]]'''

#add,del,rename on df
'''import pandas as pd
s=pd.Series{[10,11,12,13]}
df=pd.DataFrame(s)
print(df)
df.columns=['list1']
df['list2']=20
df['list3']=df['list1']+df['list2']'''


#deletion

'''import pandas as pd
s=pd.Series{[10,11,12,13]}
df=pd.DataFrame(s)
print(df)
df.columns=['list1']
df['list2']=40
df['list3']=df['list1']+df['list2']
print(df)
del df['list3']
print(df)
df.pop('list2')
print(df)
df['list4']=50
print(df)
df1=df.drop('list4',axis=1)#axis 1 is for deleting columns and 0 is for deleting row wise
print(df1)
df2=df1.drop[index=[1,3],axis=0]
print(df2)'''

#acessing using loc(),iloc(),label

'''import pandas as pd
profit={'hp':{'qter1':2500,'qtr2'=2000,'qter3'=3000,'qter4'=4000},
        'inf':{'qter1':2500,'qtr2'=2000,'qter3'=3000,'qter4'=4000},
        'tcs':{'qter1':2500,'qtr2'=2000,'qter3'=3000,'qter4'=4000}}
df=pd.DataFrame(profit)
print(df)
print(df.loc['qtr3',:])
print(df.loc['qtr1','qtr3':])
print(df.loc[:,'inf'])
print(df.loc[:,'hp':'inf'])
print(df.loc[:,:])
#iloc
print(df.iloc[0:2,1:2]0)#give index instead of name of row/column,ending index is not considered here
print(df.iloc[:,0:2])
print(df.iloc[0:1,:])
print(df.iloc[:,0:1])'''



#head(),tail()
'''import pandas as pd
empdata={'empid':[10,11,12,13,14,15],
         'ename':['sachin','bandaru','gunda','vijay','arun','varun'],
         'doj':['12-01-2013','12-01-2014','12-01-2015','12-01-2016','12-01-2017','12-01-2019']}
df=pd.DataFrame(empdata)
print(df)
print(df.head())
print(df.head(3))
print(df.tail())
print(df[2:5])
print(df[0:1])'''

#concat(),join()
'''import pandas as pd
dic1={'id':['1','2','3','4','5'],'value1':['a','c','e','g','i'],
      'value2':['b','d','f','h','j']}
dic2={'is':['2','3','6','7','8'],'value1':['k','m','o','q','s'],
      'value2':['l','n','p','r','t']}
df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)
print(df1)
print(df2)
df3=pd.concat([df1,df2])
print(df3)

df3=pd.concat([df1,df2],axis=1)
print(df3)

df3=pd.concat([df1,df2],ignore_index=True)
print(df3)'''

#CSV file ;comma seperated values ,save notepad as .csv converts to spreadsheet
#importing and exporting csv file


#import pandas
'''import pandas as pd
df=pd.read_csv("C:\\Users\\smart\\Desktop\\data1.csv")
print(df) '''              

#export df to csv
'''import pandas as pd
L=[{'name':'charan','marks':83},{'name':'ran','marks':80},{'name':'cha','marks':88},{'name':'aran','marks':87}]
df=pd.DataFrame(L)
print(df)
df.to_csv('D:\\DataFrame.csv')'''








