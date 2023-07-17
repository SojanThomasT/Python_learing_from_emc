
rcb ="win"
if (rcb =="win"):
    print("RCB won the match")
else:
    print("RCB loss the match again")

user =input()
if (user.lower() == "died"):
    print("Surya Meets Priya")
else:
    print("Surya weds Megna ")
#find pass orfail
mark = int(input("Enter Your Mark: "))
if mark >=35:
    print("You passed :)")
else:
    print("Sorry! You Failed :|")

#find eligibloity of scholarship:
income= int(input("Enter your Income: "))
if income >= 7000:
    print("Your are Not Eligible for scholarship")
else:
    print("Your are Eligible for scholarship")
# find a num is divisibile by 3
a = int(input("Enter a number"))
if a%3 == 0:
    print("the number is divisible by 3")
else:
    print("the number is not divisible by 3")

# get a number and find wheathere is devisibile by both:
num = int(input("Enter a Number: "))
if (num%5 == 0) and (num%3 == 0): #(num%5 and num%3) == 0:
    print(num, "is divisible by 3 and 5")
else:
    print(num, "this is not divisible by 3 and 5")

#get input and even or odd:
num = int(input())
if (num%2) == 0:
    print(num, "is even")
else:
    print(num, "is odd")

#get a score from user and apply condition:
score = int(input())
if score < 35:
    print("Poor Student")
elif 35<=score<70:
    print("Average Student")
elif score>=70:
    print("Good Student")

#mini calculator:
a = int(input())
b = int(input())
option = input("choose a operation add/sub/mul/div:  ")
if option.lower() == "add":
    print(a + b)
elif option.lower() == "sub":
    print(a-b)
elif option.lower() == "mul":
    print(a*b)
elif option.lower() == "div":
    print(a/b)
else:
    print("Enter Valid Option")

# getscore and eligiblity
score = int(input("Enter Your Mark: "))
if score >70:
    name=input("Enter Your Name: ")
    dept=input("Enter Your Department: ")
    loct=input("Enterb Your Location: ")
    print("You're Eligible")
else:
    print("You're not Eligible")
 
    
#get salery and age. and eligibility for loan
salery = int(input("Enter your Salery: "))
age = int(input("Enter your Age: "))
if (salery >= 20000) or (age <= 25):
    loan_amt =int(input("Enter Required Loan Amount: "))
    if loan_amt <=50000:
        print("Your ELigibile for Loan")
    else:
        print("Maximum Loan Amount is Rs:50000/- only")
else:
    print("Sorry! Your Not ELigible :|")

mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total= mark1+mark2+mark3+mark4+mark5
average= total/5
print(average)
if average<35:
    print("Additional class is required")
else:
    print("You are Good to Go")