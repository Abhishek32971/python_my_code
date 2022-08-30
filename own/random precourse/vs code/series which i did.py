#its ok to type stuff in any bravkets be it any d type
'''import pandas as pd
s1=pd.Series(('w','e','r'))
print(s1)'''

#single value in py sequence-works
'''import numpy as np
import pandas as pd
s1=pd.Series((34))
print(s1)'''

#difference between range and arange
'''import numpy as np
s1=range(2,7)
print(s1)
s2=range(3,7,2)
print(s2)
s3=np.arange(2,7)
print(s3)'''

#range and arange
'''import  numpy as np
import pandas as pd
s1=pd.Series(np.arange(3,7,2))
print(s1)'''

#using scalar value  using range
'''import pandas as pd
import numpy as np
si=pd.Series(34,index=range(1,5))
print(si)'''

#using scalar value in arange
'''import pandas as pd
import numpy as np
si=pd.Series(34,index=np.arange(1,5))
print(si)'''

#using index and data as a py sequence
#1-using none in data and index-error
'''import pandas as pd
import numpy as np
si=pd.Series(data=(1,2,3)
print(si)'''

#2-usingproper index and data
'''import pandas as pd
import numpy as np
si=pd.Series((1,2,3,4),index=(1,3,4,5))
print(si)'''

#can you specify a defined string to data without using data()-'yes'
'''import pandas as pd
import numpy as np
s1=(1,2,3,4,5)
s2=('a','b','c','d','e')
si=pd.Series(s1,index=(s2))
print(si)'''

#using mathametical expressions
'''import pandas as pd
import numpy as np
a=np.arange(2,8,2)
si=pd.Series(index=(1,2,3),data=a*2)
print(si)'''

#using 2*s1 instead of tile()-error output simply shows (4,16,4) as data
'''import pandas as pd
import numpy as np
a=np.arange(2,8,2)
si=pd.Series(data=2*a)
print(si)'''

#trial2-works as here a is a python list
'''import pandas as pd
import numpy as np
a=(1,2,3)
s1=pd.Series(data=2*a)
print(s1)'''

#does it work when syntex-a*2
'''import pandas as pd
import numpy as np
a=(1,2,3)
s1=pd.Series(data=a*2)
print(s1)'''

#does py take dtype as float by default when nan is mentioned or compulsary to specify dtype-no
import pandas as pd
import numpy as np
contri=np.array((6500,4500,4500,np.NaN))
section=('a','b','c','d')
s1=pd.Series(contri*2,index=section)
print(s1)

#type and itemsize
'''print(s1.dtype)
print(type(s1))
print(s1.itemsize)'''#error
'''print(s1.size)
print(s1.ndim)
print(s1.shape)
print(s1.nbytes)'''

#check emptiness and presence of nans
'''print(s1.empty)
print(s1.hasnans)'''

#accessing individual elements
'''print(s1[2])'''

#slicing a seriesobject
'''print(s1[1:3])
print(s1[1:4])'''

#vector operations
'''print(s1*2)
print(s1+2)
print(s1-2)
print(s1>2)
s2=s1**2
print(s2)'''

#arithamatic operations on two objects
'''print(s1*s2)
print(s1/s2)
print(s1=s2)
print(s1-s2)'''

#boolen operations on series
'''print(s1>1000)
print(s1[s1>1000])'''

# using slicing instead of reindex
'''s2=s1[::-1]
print(s2)'''

#drop a row
'''print(s1.drop('c'))'''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

