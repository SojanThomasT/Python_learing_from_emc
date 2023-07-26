#inheritance: from one to other class

class grandpa():
    def money(self):
        print("Grabdapa's Wealth")
class dad(grandpa):
    def phone(self):
        print("Dad's phone")
class mom():
    def sweets(self):
        print("Mom's Sweets")
class son(dad,mom):
    def laptop(self):
        print("Son's laptop")

#object declaration:
sojan=son()
rincy=dad()
sojan.phone()
sojan.sweets()
sojan.money() #son can asscess dad phone and also grandpa wealth boz dad has access to grandpaa,,,,

# create a class called animla with method sound() that prints "animal makes sound"./
#create a derived class called Dog that inherits from animals and overrides the sound() method to proint "Dog barks"
#create a derived class called Bird( ) that inherits from animal and overide the soundes method to print "Brids sings"
class Animals():
    def sound(self):
        print("Animal makes sound")
class Dog(Animals):
    def sound(self):
        print("Dogs Barks")
class Birds(Animals):
    def sound(self):
        print("Birds sings")
#declaring object
a1=Animals()
a1.sound()

# create a base class  called shape with method area() that returns 0. 
# create a derived class called rectange that inherits from shape and overide area() method to calculate and return area of rectangle.
class Shapes():
    def area(self):
        return "0"
class Rectangle(Shapes):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def area(self):
        return self.a*self.b
    
s1=Rectangle(10,110)
print(s1.area())


#create a base called person with a constructor that takes a name as a parameter. 
# create a derived classstudent that inherits from person and has a constructor that takes a parameter called grade
# write  amethod in student to display the name and grade using super keyword
class Person():
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        #self.name=name
        self.grade=grade
    def display(self):
        print("name of the student is {} and he scored {} grade in class".format(self.name,self.grade))

s1=Student("sojan","A+")
s1.display()

# create a base class called vechile with a method start()that prints"Vechicle started"
#create a derived class called car that inhert from velicle and overide the start() method and print "Car started"
class Vechile():
    def start(self):
        print("Vechile Started")

class Car(Vechile):
    def start(self):
        print("Car started")

i10=Car()
i10.start()

#create a base class called employee with properities name and salery. 
#create a derived class called manager that inherits from empoyee and adds a property department.
#write a method in manager to display the name, salery, department of manager
class Employee():
    def __init__(self,name,salery):
        self.name=name
        self.salery=salery
class Manager(Employee):
    def __init__(self,name,salery,dept):
        super().__init__(name,salery)
        self.dept=dept
    def display(self):
        print("the name of employee is {} , his salery is {} and he belong to {} department".format(self.name,self.salery,self.dept))

e1=Manager("sojan",25000,"Web Development")
e1.display()

        

