"""1. Create a Python class named Circle. Create 2 functions area and
perimeter. Read radius as input for both functions.

2. Create a Temperature class. Make two methods :
1. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

3. Create a class Employee with methods to assign data and print data.
4. Create class named Student. Write methods to read marks as input and
return total as output. Another method to take total and number of subject
as input and return average.

py 13 part 2(oops)
1. Create a class Banking. Constructor to assign account balance. Create
methods to deposit and withdraw. Minimum account balance should be
Rs.500.
2. Create a child class as Saving Account for Banking. Add method to
calculate interest. For account balance greater than 25000, interest of
6.5% should be added with account balance.
3. Write a class with constructor. Initialize 2 numbers in constructor. Write
methods to return quotient(both division and floor division) and reminder
of those 2 numbers.
4. Initialize radius in constructor and rewrite Circle class from Py10 Part 1

py 14 part 1(oops)
1. Create class Employee with name, Id, designation,
department as members. Also create separate class for Salary. Properties
in salary class are basic pay, hra , pf , insurance. Write methods to read
values for all properties and separate method to display that.
2. A bank maintains two kinds of accounts – Savings account and Current
account. The savings account provides simple interest, deposit and
withdrawal facilities. The current account only provides deposit and
withdrawal facilities. Using inheritance write program for the same.

py 14 part 2(oops)
Design java application to model Employee of an “ABC” organization.
Consider types of employees as
a. Manager
b. Sales Person
Perform the following
a. Implement simple inheritance where Employee (employee ID, First
Name, Last
Name, Current salary) is super class.
b. Consider Manager (number of stock options) and SalesPerson
(number of sales,
commission rate) as subclasses.
2. Using encapsulation get the employee basic salary, bonus, loss of pay and
calculate the total salary.
3. Write a program using Hierarchical Inheritance.
"""
#Write abstract base class for employee. Include abstract methods for
#salary() and attendance(). Create 2 derived classes Marketing and Part
#time employees and implement both functions.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def salery(self):
        pass
    def attendance(self):
        pass

class marketing_employee(Employee):

    def __init__(self,name,sales_done):
        self.name= name
        self.sales_done=sales_done
    def salery(self):
        self.monthly_salery=8000+(self.sales_done*40)
        return self.monthly_salery
    def attendance(self):
        return "Present"
class part_time_employee(Employee):
    def __init__(self,name,sales_done_per_day):
        self.name=name
        self.sales_done_per_day=sales_done_per_day
        self.hourly_rate=8*5
    def salery(self):
        self.monthly_salery=2000+(self.sales_done_per_day*self.hourly_rate)
        return self.monthly_salery
    def attendance(self):
        return "Present"
    def display(self):
        print("name: {}".format(self.name))
        print("salery {}".format(self.salery()))
        print("attendence {}".format(self.attendance()))

    

me1=marketing_employee("sojan",6)
print("name: {}".format(me1.name))
print("salery {}".format(me1.salery()))
print("attendence {}".format(me1.attendance()))
pt1=part_time_employee("sony",2)
pt1.display()
"""
#Create an abstract class Shapes with an abstract method as findarea().
#Create separate classes Circle, Square, Rectangle and implement
#findarea()
from abc import ABC, abstractmethod
import math

class Shapes(ABC):

    @abstractmethod
    def findArea(self) -> float:
        pass

class Circle(Shapes):

    def __init__(self):
        self.r = float(input("Enter radius value: "))

    def findArea(self):
        return math.pi * self.r ** 2

class Square(Shapes):

    def __init__(self):
        self.a = float(input("Enter side length: "))

    def findArea(self):
        return self.a ** 2

class Rectangle(Shapes):

    def __init__(self):
        self.a = float(input("Enter length: "))
        self.b = float(input("Enter width: "))

    def findArea(self):
        return self.a * self.b

# Example usage:

def find_area():
    print("Choose the shape to find area:")
    print("1 for square")
    print("2 for circle")
    print("3 for rectangle")

    choice = int(input())

    shape = None
    if choice == 1:
        shape = Square()
    elif choice == 2:
        shape = Circle()
    elif choice == 3:
        shape = Rectangle()
    else:
        print('Invalid choice')
        return

    area = shape.findArea()
    print("The area is", area)

find_area()




#Create a class Gmail with login method. Create 2 different methods
#named as login(). One method should be taking username and password
#as input. Another method with password only as input.
class Gmail():
    def __init__(self):
        print("Welcome to Gmail.com")
    def login(self, username=None, password=None):
        if (username is not None) and (password is not None):
            print("Logging with username {} and password".format(username)) 
        elif (password is not None):
            print("Logging with password")
        else:
            print("Invalid Login Details")

de1=Gmail()
de1.login(username="sojan@gmail.com",password="@@@@@@")
de1.login(password="@#@#@#")

#Create a base class Employee and get staff id, name, basic, salary, loss of
#pay from the user. Create a sub class Trainee extends Employee and get
#incentives and calculate net pay print it using method overriding.
class Employee():
    def __init__(self):
        #asking input from user:
        self.id=input("Enter your id: ")
        self.name=input("Enter your Name: ")
        self.basicpay=float(input("Enter your basic pay: "))
        self.loss_of_pay = float(input("Enter Loss Of Pay if any :"))
    def netpay(self):
        self.salery=self.basicpay-self.loss_of_pay

class Trainee(Employee):
    def __init__(self):
        super().__init__()
        self.incentives=float(input("Enter your incentives: "))
    def netpay(self):
        super().netpay()
        self.takehome=self.salery+self.incentives

    def display(self):
        print("The Name of the employee is {} and his id is {} hois take home salery id {}".format(self.name,self.id,self.takehome))
        print("Detailed List")
        print("Staff ID:", self.id)
        print("Name:", self.name)
        print("Basic Salary:", self.basicpay)
        print("Loss of Pay:", self.loss_of_pay)
        print("Incentives:", self.incentives)
        print("Net Pay:", self.takehome)

t1=Trainee()
t1.netpay()
t1.display()

"""

