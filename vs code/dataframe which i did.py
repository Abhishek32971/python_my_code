#creating dataframe
'''import pandas as pd
import numpy as  np
data={'students':('ruchika','neha','mark','gurjyot','jamal'),'marks':(21.3,85.5,74,88.5,89),'sports':('cricket','badminton','athletics','kabbadi','something else')}
df1=pd.DataFrame(data)
print(df1)'''

#creating dataframe with index
'''import pandas as pd
import numpy as  np
data={'students':('ruchika','neha','mark','gurjyot','jamal'),'marks':(21.3,85.5,74,88.5,89),'sports':('cricket','badminton','athletics','kabbadi','something else')}
df1=pd.DataFrame(data,index=('a','b','c','d','e'))
print(df1)'''

#dataframe from 2d dictionary having values as dictionary objects
#ex1-crate dataframe with rows -yr1 and yr2 and columns qtr1,2,3,4
'''import pandas as pd
import numpy as np
df1=pd.DataFrame({'year1':{'qtr1':123,'qtr2':234,'qtr3':345,'qtr4':567},'year2':{'qtr1':222,'qtr2':333,'qtr3':444,'qtr4':555}})
print(df1) '''                

#2d dataframe from a list of lists/dictionaries
'''import numpy as np
import pandas as pd
toppera={'roll':115,'name':'shashi','marks':97.5}
topperb={'roll':114,'name':'shugan','marks':98.5}
topperc={'roll':116,'name':'shashu','marks':99.5}
topper=(toppera,topperb,topperc)
df1=pd.DataFrame(topper)
print(df1)'''

#dataframeusing lists
'''import pandas as pd
import numpy as np
listt=((1,2,3),(2,3,4),(3,4,5))
df1=pd.DataFrame(listt)
print(df1)'''

#adding index to it
'''import pandas as pd
import numpy as np
listt=((1,2,3),(2,3,4),(3,4,5))
df1=pd.DataFrame(listt,index=('a','s','d'))
print(df1)'''

#adding column name
'''import numpy as np
import pandas as pd
list1=((1,2,3),(2,3,4),(3,4,5))
df1=pd.DataFrame(list1,columns=['a','b','c'],index=['yes','no','whatever'])
print(df1)'''

#dataframes using 2d arrays
'''import pandas as pd
import numpy as np
lists=np.array([[1,2,3],[2,3,4]])
l=pd.DataFrame(lists)
print(l)'''

#datatype if 2 series are given
'''import pandas as pd
import numpy as np
num1=pd.Series((2,3,4,5))
num2=pd.Series((3,4,5,6))
df1=pd.DataFrame({'people':num1,'people2':num2})
print(df1)'''

#creating a dataframe from existing one with same values
'''df2=pd.DataFrame(df1)
print(df2)'''

-----------------------------------------------------------------------------------------------

#Attributes



