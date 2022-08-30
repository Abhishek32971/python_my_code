import re
s="Welcome to REVA University"
patt="(a|e|i|o|u|A|E|I|O|U)"
count=0
l=list()
for i in s:
    if re.search(patt,i):
        count+=1
        l.append(i)
print(count,l)

