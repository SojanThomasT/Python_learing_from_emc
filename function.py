"""
#write a function to add, sub, mul, div:
#then get input from user
#defining function
def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
#coding:
a=int(input())
b=int(input())
option=input("do u want to add or substract or multiply or divide: ")
if option.lower() == "add":
    sum(a,b)elif option.lower() == "substract":
    sub(a,b)
elif option.lower() == "multiply":
    mul(a,b)
elif option.lower() == "divide":
    div(a,b)
else:
    print("Please Enter Valid Option")

#defining a function to find a given number is even or not
def findevenorodd(a):
    if (a%2 == 0):
        print(a, "is even number")
    else:
        print(a, "is odd number")
findevenorodd(13)

#get a input from user  and find wheather  the student is pass or fail
def passorfail(num):
    if num>=35:
        print("congrates! you passed the exam")
    else:
        print("Sorry! Better luck next time")
a=int(input("Enter YOur mark: "))
passorfail(a)

#  get two input from user and print it range:
def printrange(a,b):
    for i in range(a,b):
        print(i, end=", ")
a=int(input())
b=int(input())
printrange(a,b)

#{Create a function to read a list as input and return maximum
#number as output. Call this function and find second maximum
#number.}
my_list=[
]
new_my_list=[]

def userinput():
    n=int(input("TOtal number of value"))
    for i in range (n):
        num=int(input("enter a number: "))
        my_list.append(num)
    print(my_list)

def decending_order():
    global new_my_list
    new_my_list = sorted(my_list,reverse=True) # to store a list in new variable
    #mylist.sort(reverse=true) ---. to store in same variable:
    print(new_my_list)
def secondmax():
    a = new_my_list[1]
    print("second largest is",a)

userinput()
decending_order()
secondmax()

#3. Write function to read a number as input and return digits as list.
n=input("enter a number: ")
digit_list=[]
def num_to_digit():
    for i in n:
        digit_list.append(i)


num_to_digit()
print(digit_list)



#2. Create functions to add(), subtract(), divide() and multiply(). All
#functions should read 2 values as input.#Read bill amount as input.
#Calculate 12% of GST amount. Find total amount to be paid. Read
#number of EMIs. Find emi amount to be paid per month. 
def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
Bill_Amount  = int(input("Enter a Bill Amount: "))
GST_Amount = mul(Bill_Amount,div(12,100))
Total_Amount = add(Bill_Amount,GST_Amount)
EMI = int(input("Enter a Number of EMI Required: "))
Due_Amount=div(Total_Amount,EMI)
print("BILL AMOUNT: ",Bill_Amount)
print("12% GST is: ", GST_Amount)
print("TOTAL AMOUNT TO BE PAID IS : ", Total_Amount)
print("TOTAL NUMBER OF EMI IS: ", EMI)
print("DUE AMOUNT IS: ",Due_Amount)

#write a function to find a factiorial of given number:
def factorial(num):
    global initial
    initial=1
    while num >=1:
        initial=initial*num
        num-=1
    #return initial

factorial(5)
print(initial)

#check for validation

s_user_name = "sojan thomas"
s_password = "1234"
name=input("Enter UserName: ")
password=input("Enter Password :")

def validation():
    if (s_user_name == name.lower()) and (s_password == password):
        return True
    else:
        return False
    
print(validation())
"""
#(a+b)*c
num1=int(input())
num2=int(input())
num3=int(input())
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
x=add(num1,num2)
print("addition is",x)
y=mul(x,num3)
print("multiplication is",y)