
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

mark = int(input("Enter Your Mark: "))
if mark >=35:
    print("You passed :)")
else:
    print("Sorry! You Failed :|")

    
income= int(input("Enter your Income: "))
if income >= 7000:
    print("Your are Not Eligible for scholarship")
else:
    print("Your are Eligible for scholarship")



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
