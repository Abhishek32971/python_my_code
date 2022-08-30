# creating series using list 

'''import pandas as pd
data=[10,20,30,40,50]
S=pd.Series(data)
print(S)
print(type(data))
print(type(S))'''

# creating series using nd array
'''import pandas as pd
import numpy as np
arr=np.array([10,20,30,40])
print(arr)
print('**************')
S=pd.Series(arr,index=['a','b','c','d'])
print(S)'''

# otherway to maake in series
'''import pandas as pd
import numpy as np
arr=np.arange([10,20,30,40])
print(arr)
print('**************')
S=pd.Series(arr,index=['a','b','c','d'])
print(S)'''

# for emptyseries
'''import pandas as pd
S=pd.Series()
print(S)'''

#using scalar value
'''import pandas as pd
d=50
S=pd.Series(d,index=[1,2,3,4,5])
print(S)'''

# using dictionary
'''import pandas as pd
d={'name':'harini','sub':'ip','marks':89}
print(d)
print('ichwdcdcwwjncjwdd')
S=pd.Series(d)
print(S)'''

#mathamatical operation on list
'''import pandas as pd
impoet numpy as np
L=[1,2,3,4]
L1=[5,6]
print(L)
print(L+L1)
print(L*2)'''

#mathamatical operation on list
'''import pandas as pd
import numpy as np
L=[1,3,5,7,9]
S=pd.Series(L)
print(S)
print("addition")
print(S+2)
print("multiplication")
print(S*2)
print("squaring")
print(S**2)
S1=S**2
print(S1[S1>50])'''

# ex2
'''import pandas as pd
import numpy as np
L1=[1,2,3,4,5]
S1=pd.Series(L1,index=['a','b','c','d','e'])
arr1=np.arange(2,11,2)
S2=pd.Series(arr1,index=['a','b','c','d','e'])
S3=pd.Series([5,14,23,34],index=['a','b','c','d'])
print(S1)
print('ewccvreeregeveveveverv')
print(S2)
print('ewccvreeregeveveveverv')
print(S3)
print('ewccvreeregeveveveverv')
print('addition')
print(S1+S2)
print('ewccvreeregeveveveverv')
print(S2+S3)
print("filling thr given val using fill function")
print(S2.add(S3,fill_value=2))
print(S2.add(S3))
print(S1.mul(S2))'''
#the programme automatically fills nan in missingplace and when a value is speified it adds it to the defaulted "10"



#Head function used to extractfirst five values of series
'''print[S1.head()]
print[S2.head(2)]'''

#tail function
'''print[S1.tail()]
print[S2.tail(3)]
'''

#selection in Series
'''import pandas as pd
import numpy as np
L1=[1,2,3,4,5]
S1=pd.Series(L1)
arr1=np.arange(2,11,2)
S2=pd.Series(arr1)
print[S1]
print[S1.loc[:2])
print[S2.iloc[:2])
'''

#selection using index
'''import pandas as pd
import numpy as np
L1=[1,2,3,4,5]
S1=pd.Series(L1,index=['a','b','c','d','e'])
arr1=np.arange(2,11,2)
S2=pd.Series(arr1,index=['a','b','c','d','e'])
S3=pd.Series([5,14,23,34],index=['a','b','c','d'])
print(S1)
print(S1[2:4])
print(S1[2])'''

#indexing in series
'''import pandas as pd
L=[1,3,5,7,9]
S=pd.Series(L,index=['first','second','third','forth','five'])#number of element should match no of index
print(S)'''

#slicing in series
import pandas as pd
import numpy as np
arr=np.arange(1,11,1)
print(arr)
S=pd.Series(arr)
print(S)
print(S[1:5:2])
print(S[0:7:3])
