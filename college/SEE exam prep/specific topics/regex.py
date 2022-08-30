'''
import re
pattern='^a.s$'
test_string='abs'
result=re.match(pattern,test_string)
if result:
    print("success")
else:
    print("fail")
s=re.search(pattern,test_string)
if s:
    print("success")
print(re.search(pattern,test_string))
print(re.match(pattern,test_string))
print(result.start())
print(result.group())
'''


'''
import re 
pattern='python'
str1='abbs python'
result=re.match(pattern,str1)
print(result)
print(result.group())
'''


