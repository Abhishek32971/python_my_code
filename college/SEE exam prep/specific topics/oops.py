'''
class MyClass:
    #This is my second class
    a=10
    def func(self):
        print("Hi ECE")
print(MyClass.a)
print(MyClass.func)
print(MyClass.__doc__)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def output(self):
        print("the output is ",self.name,self.age)

p=person("abhi",18)
p.output()
print(p.age,p.name)


class car:
    def __init__(self,company_name,model,color,manufacturing_year,price):
        self.company_name=company_name
        self.model=model
        self.color=color
        self.manufacturing_year=manufacturing_year
        self.price=price
    def desplay__car__details(self):
        print("the car details are :",self.company_name,self.model,self.color,self.price,self.manufacturing_year)

carobject=[]
n=int(input("enter the number of cars you want to enter"))
for i in range(n):
    company_name=input("enter the name of the comp")
    model=input("enter the model name")
    color=input("enter the color")
    manufacturing_year=(input("enter the maufacturing year"))
    price=int(input("enter the price"))
    carobject.append(car(company_name,model,color,manufacturing_year,price))

print("car details are")
for obj in carobject:
    obj.desplay__car__details()



Airlineobject=[ ]
class ARS:
    def __init__(self,name,source,destination,travel_date):
        self.name=name
        self.source=source
        self.destination=destination
        self.travel_date=travel_date
    def display_pass_details(self):
         print(self.name,"\t",self.source,"\t",self.destination,"\t",self.travel_date)



#input 

Airlineobject.append(ARS("Sachin","bangalore","USA","1/oct/2020"))
Airlineobject.append(ARS("Dravid","bangalore","London","2/oct/2020"))
Airlineobject.append(ARS("Rahul","bangalore","China","3/oct/2020"))
Airlineobject.append(ARS("Kiran","bangalore","London","5/oct/2020"))
Airlineobject.append(ARS("Supreeth","USA","China","10/Feb/2020"))

print("Details of the Passenger who travelled from bangalore to London is \n")
for i in range(0,len(Airlineobject)):
    if((Airlineobject[i].source=="bangalore") and (Airlineobject[i].destination=="London")):
        Airlineobject[i].display_pass_details()
print("\n")

for i in Airlineobject:
    if i.source=="banglore" and i.destination=="London":
        i.display_pass_details()
print("\n")

print("Details of the Passenger who travelled from USA to China on 10th Feb 2020 is \n")
for i in range(0,len(Airlineobject)):
    if((Airlineobject[i].source=="USA") and (Airlineobject[i].destination=="China") and Airlineobject[i].travel_date=="10/Feb/2020"):
        Airlineobject[i].display_pass_details()




#encaptulation

class computer:
    def __init__(self):
        self.__maxprice=900
    
    def sell(self):
        print("selling price is ",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
    
c1=computer()
c1.sell()
c1.__maxprice=1000
c1.sell()
c1.setmaxprice(1000)
c1.sell()


from abc import ABC,abstractmethod
class Polygon:         
    @abstractmethod
    def sides(self)
      pass  
  
class Triangle(Polygon):   
   def sides(self):   
      print("Triangle has 3 sides")   

class Pentagon(Polygon):   
   def sides(self):   
      print("Pentagon has 5 sides")   
t = Triangle( )   
t.sides()   
p = Pentagon( )   
p.sides()    




class User:
    #Program to demonstrate single inheritance
    def __init__(self,name):
        self.name=name
    def printname(self):
        print("Name = " + self.name)
class programmer(User):
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Programming Python")
u1=User("shiva")
u1.printname( )
u2=programmer("supreeth")
u2.printname()
u2.display( )

'''

class parrot():
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrots cant swim")
class penguine():
    def fly(self):
        print("penguine cant fly")
    def swim(self):
        print("penguine can swim")
def flyintest(bird):
    bird.fly()

p=parrot()
pe=penguine()
flyintest(p)
flyintest(pe)