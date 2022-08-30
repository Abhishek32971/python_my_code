'''class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("the name:{} \n the age {}".format(self.name,self.age))

obj1=person("sachin",46)
obj1.display()'''


'''class complex():
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def display(self):
        print("{}+{}j is the complex you entered".format(self.real,self.img))
obj1=complex(1,2)
obj1.display()'''


'''class car:
    def __init__(self,cmpn,mdl,clr,mfy,price):
        self.cmpn=cmpn
        self.mdl=mdl
        self.clr=clr
        self.mfy=mfy
        self.price=price
    def display(self):
        print("the details are companyname={}\nmodel={}\ncolor={}\nmanufacturingyear={}\nprice={}\n".format(self.cmpn,self.mdl,self.clr,self.mfy,self.price))
carobj=[]
n=int(input("enter the number of cars you want to enter\n"))
for i in range(n):
    cmpn=input("enter the company name")
    mdl=input("enter the model")
    clr=input("enter the model")
    mfy=input("enter the manufacturing year")
    price=input("enter the price")
    carobj.append(car(cmpn,mdl,clr,mfy,price))

for obj in carobj:
    obj.display()'''

'''Airlineobject=[ ]
class ARS:
    def __init__(self,name,source,destination,travel_date):
        self.name=name
        self.source=source
        self.destination=destination
        self.travel_date=travel_date
    def display_pass_details(self):
         print(self.name,"\t",self.source,"\t",self.destination,"\t",self.travel_date)
Airlineobject.append(ARS("Sachin","bangalore","USA","1/oct/2020"))
Airlineobject.append(ARS("Dravid","bangalore","London","2/oct/2020"))
Airlineobject.append(ARS("Rahul","bangalore","China","3/oct/2020"))
Airlineobject.append(ARS("Kiran","bangalore","London","5/oct/2020"))
Airlineobject.append(ARS("Supreeth","USA","China","10/Feb/2020"))

for i in Airlineobject:
    if i.source=="bangalore"and i.destination=="London":
        i.display_pass_details()
'''

'''class user:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class programer(user):
    def disp1(self):
        print("programer")


p1=programer("jake")
p1.display()
'''

'''class computer:
    def __init__(self,price,model):
        self.model=model
        self.__price=price
    def disprice(self):
        print(self.__price)
    def chngprice(self,price):
        self.__price=price

c=computer(3434,"lkjkj")
c.__price=2323
c.disprice()
c.__price=3434
c.disprice()
c.chngprice(343455)
c.disprice()
print(c)'''





'''class dog:
    def __init__(self,name,color,mood,height):
        self.name=name
        self.color=color
        self.__mood=mood
        self.__height=height
    
    def change_mood(self,mood):
        self.__mood=mood
    
    def change_height(self,height):
        self.__height=height

    
    def details(self):
        print(self.name,self.__mood,self.__height)
    
g=dog("bab","bab","bab","bab")
g.details()
g.change_mood("box")
g.details()
g.kill_dog()
g.details()'''

'''class student:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    
class section():
    def __init__(self,stuobj):
        self.stuobj=stuobj
    def display(self):
        for i in self.stuobj:
            print(i.name,i.age,i.height)
    def tallest(self):
        x=self.stuobj[0]
        for i in self.stuobj:
            if i.height>x.height:
                x=i
        print("the tallest one is {} age {} height {}".format(x.name,x.age,x.height))

def addstu():
    x=input("do you want to enter student details(Y/N)")
    if x=="Y":
        studentobj=[]
        n=int(input("enter the number of values to enter"))
        for i in range(n):
            name =input("enter name")
            age=input("enter age")
            height=int(input("enter height"))
            studentobj.append(student(name,age,height))
        return studentobj
x=addstu()
y=section(x)
y.display()
y.tallest()
'''






            
    
