#line graph
'''import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,3,4]
plt.plot(x,y,'r')
plt.show()'''


#2

'''import matplotlib.pyplot as plt
x=[10,20,30,40,50]
y=[65,98,170,220,310]
plt.xlabel('overs')
plt.ylabel('score')
plt.title('ind vs eng')
plt.plot(x,y,'b')
plt.show()'''

#3
'''import matplotlib.pyplot as plt
x=[10,20,30,40,50]
y=[65,98,170,220,310]
plt.xlabel('overs')
plt.ylabel('score')
plt.title('ind vs eng')
plt.plot(x,y,marker='+',markersize='15',markeredgecolor='red')
plt.show()'''

#4

'''import matplotlib.pyplot as plt
x=[10,20,30,40,50]
y=[65,98,170,220,310]
plt.xlabel('overs')
plt.ylabel('score')
plt.title('ind vs eng')
plt.plot(x,y,'g',linewidth=5,linestyle='dashed')
plt.show()'''

#2 plots
'''import matplotlib.pyplot as plt
year=[2014,2015,2016,2017,2018,2019]
kv=[90,95,85,78,89,65]
sc=[92,85,80,98,75,66]
plt.plot(year,kv,'r')
plt.plot(year,sc,'g')
plt.xlabel('year')
plt.ylabel('pass pecentage')
plt.title('pass per kv vs sc')
plt.legend(('kv','sc'),loc='upper right',frameon=True)
plt.show()'''

#bar graph
'''import matplotlib.pyplot as plt
overs=['1-10','11-20','21-30','31-40','41-50']
runs=[65,55,70,50,80]
plt.bar(overs,runs)
plt.xlabel('over interval')
plt.ylabel('runs scored')
plt.title('ind vs aus')
plt.show()'''

#2
'''import matplotlib.pyplot as plt
overs=['1-10','11-20','21-30','31-40','41-50']
runs=[65,55,70,50,80]
plt.bar(overs,runs,width=[0.3,0.4,0.5,0.6,0.7],color='g')
plt.xlabel('over interval')
plt.ylabel('runs scored')
plt.title('ind vs aus')
plt.show()'''


#3 more colours!!!!!
'''import matplotlib.pyplot as plt
overs=['1-10','11-20','21-30','31-40','41-50']
runs=[65,55,70,50,80]
plt.bar(overs,runs,width=[0.3,0.4,0.5,0.6,0.7],color=['g','r','y','m','b'])
plt.xlabel('over interval')
plt.ylabel('runs scored')
plt.title('ind vs aus')
plt.show()'''

#4 horixontal
'''import matplotlib.pyplot as plt
overs=['1-10','11-20','21-30','31-40','41-50']
runs=[65,55,70,50,80]
plt.barh(overs,runs,width=[0.3,0.4,0.5,0.6,0.7],color=['g','r','y','m','b'])
plt.xlabel('over interval')
plt.ylabel('runs scored')
plt.title('ind vs aus')
plt.show()'''

#5
'''import matplotlib.pyplot as plt
import numpy as np
overs=['1-10','11-20','21-30','31-40','41-50']
runs=[65,55,70,50,80]
index=np.arange(len(overs))
plt.bar(overs,runs)
plt.xlabel('over interval')
plt.ylabel('runs scored')
plt.title('ind vs aus')
plt.xticks(index,overs,fontsize=20,rotation=30)
plt.show()'''


#hw
'''import matplotlib.pyplot as plt
subjects=['math','phy','chem','social','science']
x=[85,87,89,98,78]
x3=[65,37,99,78,78]
x1=[85,97,89,88,78]
plt.plot(subjects,x,'g')
plt.plot(subjects,x1,'b')
plt.plot(subjects,x3,'y')
plt.xlabel('subjects')
plt.ylabel('marks')
plt.show()'''

#5
'''import matplotlib.pyplot as plt
import numpy as np
d1=[50,60,70,80,90]
d2-[50,65,75,85,95]
x=np.linespace(1,51,5)
plt.bar(x,d1,width=3,color='r',label='tcs')
plt.bar(x,d2,width=3,color='g',label='hp')
plt.xlabel('interval',fontsize=15)
plt.ylabel('no of sales',fontsize=20)
plt.title('sales chart of company')
plt.legend()
plt.show'''

#histogram -1
'''import matplotlib.pyplot as plt
age=[22,32,35,445,55,14,26,19,56,48,33,38,28]
years=[0,10,20,30,40,50,60]
plt.hist(age,bins=years,color='r',edgecolor='black')
plt.xlabel('emp age')
plt.ylabel('number of emp')
plt.title('chaitanya college')
plt.show()'''

#write  to crate histogram by collecting ages of each citizen in a nation and display how many citizens r there in the range of0-80 yrs interval of 10

import matplotlib.pyplot as plt
age=[11,22,34,4,45,25,65,55,9,22,34,59,76,23,43]
years=[0,10,20,30,40,50,60,70,80]
plt.hist(age,bins=years,color='r',histype='bar',edgecolor='black')
plt.xlabel('age of citizen')
plt.ylabel('number of citizens')
plt.title('chaitanya college')
plt.show()

#diplay only line
'''import matplotlib.pyplot as plt
age=[11,22,34,4,45,25,65,55,9,22,34,59,76,23,43]
years=[0,10,20,30,40,50,60,70,80]
plt.hist(age,bins=years,color='r',histtype='step',edgecolor='black')
plt.xlabel('age of citizen')
plt.ylabel('number of citizens')
plt.title('chaitanya college')
plt.show()'''

#width between graphs
'''import matplotlib.pyplot as plt
age=[11,22,34,4,45,25,65,55,9,22,34,59,76,23,43]
years=[0,10,20,30,40,50,60,70,80]
plt.hist(age,bins=years,color='r',histtype='bar',edgecolor='black',rwidth=.6)
plt.xlabel('age of citizen')
plt.ylabel('number of citizens')
plt.title('chaitanya college')
plt.show()'''

#saving graphas pdf
import matplotlib.pyplot as plt
age=[11,22,34,4,45,25,65,55,9,22,34,59,76,23,43]
years=[0,10,20,30,40,50,60,70,80]
plt.hist(age,bins=years,color='r',histtype='bar',edgecolor='black')
plt.xlabel('age of citizen')
plt.ylabel('number of citizens')
plt.title('chaitanya college')
plt.savefig('D:\Histogram.jpg')
plt.show()
