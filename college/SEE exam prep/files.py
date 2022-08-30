'''fh=open("mbox.txt","w+")
fh.write("ok here goes nothing")
print(fh.tell())
fh.seek(0)
print(fh.read(20))

srn="kjkj"
name="kjkjjk"
sem="kjii"
sec="j"
avgmark="45"
fh.writelines(srn+"  "+name+"  "+sem+"  "+sec+"  "+avgmark+"\n")

fh.seek(0)'''

from re import L


fh=open("emp.txt","w+")
def entervalues(n):
    empcode,empname,basicsalary,da,lic,pf=input("enter the details(6)").split()
    totald=int(lic)+int(pf)
    gras=int(basicsalary)+int(da)
    netsal=int(gras)-int(totald)
    return (empcode+" "+empname+" "+basicsalary+" "+da+" "+lic+" "+pf+" "+str(totald)+" "+str(gras)+" "+str(netsal)+" ")

p=input("do you want to enter new values(Y/N)")
if p=="Y":
    n=int(input("enter the number of values ot add"))
    for i in range(n):
        l=entervalues(n)
        fh.writelines(l)
    fh.seek(0)
    
