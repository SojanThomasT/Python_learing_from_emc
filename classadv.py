"""
class laptop:
    def __init__(self,price,ram,processor):
        self.price=price
        self.ram=ram
        self.processor=processor
    def specification(self,brand):
        print("the specification of {} is {},{} and {}".format(brand,self.price,self.ram,self.processor))

#creating object:

hp=laptop(500000,"8gb","i5")

dell=laptop(650000,"8gb","i7")
#calling function using display
hp.specification("HP")
dell.specification("DELL")




class student:
    def __init__(self,name, register_no):
        self.name=name
        self.reg_no=register_no
    def display(self):
        print("Name fo the student is {} and his register number is {}".format(self.name,self.reg_no))

#creating object
s1=student("sojan",636015)
s2=student("sony",636016)
s1.display()
s2.display()

class fruits:
    def __init__ (self ,name, color ):
        self.name=name
        self.color = color
        print("the name of the fruit is {} and it is in {} color".format(self.name,self.color))

#creating object:
f1=fruits("apple", "red")
print(f1.name, f1.color)

class teacher:
    def __init__(self,name,sub,reg_no):
        self.name=name
        self.subject=sub
        self.register_no=reg_no
    def display(self):
        print("The name of the teacher is {} , he is handling {} and his register number is {} ".format(self.name,self.subject,self.register_no))

#creating object:
t1=teacher("sojan","maths",1234)
t2=teacher("sony","physics",1233)
t3=teacher("arun","english",1232)
my_list=[t1,t2,t3]
for i in my_list:
    i.display()

class calculator:
    def __init__(self,a,b,action):
        self.a=a
        self.b=b
        self.action= action.lower()
    def calculate(self):
        if self.action=="add":
            return self.add()
        elif self.action=="sub":
            return self.sub()
        elif self.action=="mul":
            return self.mul()
        elif self.action=="div":
            if self.b!=0:
                return self.div()
            else:
                return ("Not possible to perfrm such operation")
         
        else:
            return 'invalid option. please select "add", "sub","mul","div"'
    
    def add(self):
        self.c=self.a+self.b
        return "the addition of given two number is {}".format(self.c)
        
    def sub(self):
        self.c=self.a-self.b
        return "the substraction of given two number is {}".format(self.c)
    def mul(self):
        self.c=self.a*self.b
        return "the multiplicaion of given two number is {}".format(self.c) 
    def div(self):
        self.c=self.a/self.b
        return "the division of given two number is {}".format(self.c)

s1=calculator(2,3,"add")
s2=calculator(2,3,"sub")
s3=calculator(2,3,"muL")
s4=calculator(2,3,"Div")
s5=calculator(2,0,"div")
s6=calculator(2,3,"AMN")
my_list=[s1,s2,s3,s4,s5,s6]
for i in my_list:
    print(i.calculate())


class phone:
    charger="C-Type" #class variable
    def __init__(self,model,price):
        self.model=model #instance variable
        self.price=price #instance variable

    def display(self,brand):
        return "the model {} is from the brand {} and it is rupees {}  and it support {} charging".format(self.model,brand,self.price,self.charger)
#declaring class variable outside:
phone.charger="B-Type"
#object creation
s1=phone("X1001",23000)
s2=phone("X1002",25000)
my_list=[s1,s2]
for i in my_list:
    print(i.display("samsung"))
"""
class phone:
    charger_type="C-Type"
    def __init__(self):
        self.brand=""
        self.price=12000
    def set_price(self,price):
        self.price=price
    def get_price(self):
        print(self.price)
        print(self.brand,self.price,self.charger_type)
    #declaring class variable
    @classmethod
    def set_charger_type(cls):
        cls.charger_type="p-Type"
        print("charger type changed")
    @staticmethod # to avoid self variable
    def info():
        print("this is a information page")


#declaring object:
hp=phone()
hp.get_price()
hp.set_price(23000)
hp.get_price()
hp.set_charger_type()
hp.get_price()
phone.set_charger_type() #getting error as saying declaring class
#phone.set_charger_type(phone) # to avoid redclaring the objec nam ewe are using @
hp.info()