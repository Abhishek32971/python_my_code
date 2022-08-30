import re


patt1="[abc]"
string1="aaaa"
string2="bbb"
string3="ccc"
if re.search(patt1,string1):
    print("a ok")
print(re.search(patt1,string2))
print(re.search(patt1,string3))



patt1=".."
string1="abc"
string2="ab"
string3="a"

if re.search(patt1,string1):
    print("a ok")
if re.search(patt1,string2):
    print("a ok")
if re.search(patt1,string3):
    print("a ok")



patt1="\Bfoo"
string1="afoo"

if re.search(patt1,string1):
    print("a ok")




print(re.match(patt1,string1))
print("match case found")
n=re.search(patt1,string1)
print(n.start(),n.span(),n.group(),n.end(),len(string1))




patt1="\w+"
string1='shiv13W'
if re.search(patt1,string1):
    print("a ok")



patt1="(0|91)?[0-9]{10}"
string1="9999999"
if re.match(patt1,string1):
    print("number match")



