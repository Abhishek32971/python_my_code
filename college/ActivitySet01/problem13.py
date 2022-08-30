import re
fie=open("data.txt")
regex="\d+"
sum=0
for l in fie:
    lst=re.findall(regex,l)
    for i in lst:
        sum+=int(i)
print(sum)