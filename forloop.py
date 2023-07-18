
#printing 32 tables:
n=int(input("Enter a Number to find multiplication tables: "))
for i in range (1,11):
    print(n,"X",i,"=",n*i)
#get two number and print number btw them:
i = int(input("enter 1st number: "))
j = int(input("enter second number: "))
for x in range (i+1, j):
    print(x)
    
#print even number btw 1 to 10:
n=int(input())
list1=[]
count=0
for i in range(1,n+1):
    if i%2 == 0:
        list1.append(i)
        count+=1    #count=count+1
    else:
        pass
print(len(list1))
print(count)

#count even and odd number
n=int(input())
even_no=[]
odd_no=[]
count=0
for i in range(1,n+1):
    if i%2 == 0:
        even_no.append(i)
    else:
        odd_no.append(i)
        pass
print(len(even_no))
print(len(odd_no))

#Write a Python program to display all the elements in a list using a for loop.
my_list=["hi","hello","I'm","sojan"]
for i in my_list:
    print(i)
    
#Write a Python program to find the factorial of a number using a for loop.
n=int(input())
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)

#Write a Python program to check if a given string is a palindrome using a for loop.

#Write a Python program to calculate the average of numbers in a list using a for loop.
list1=[2, 45, 85, 55]
sum=0
for i in list1:
    sum+=i
print(sum)

#Write a Python program to find the largest element in a list using a for loop.
my_list=[22,43,56,11,45,99,67,98,11,10,12,90,23]
a=0
for i in my_list:
    if i>a:
        a=i
    else:
        pass
print(a)

#Write a Python program to count the number of vowels in a string using a for loop.
vowels=['a','e','i','o','u']
count=0
a=input("enter string:")
for i in a:
    if i in vowels:
        count+=1
print(count)
#Write a Python program to print a triangle of asterisks using a for loop.

n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),'*'*((2*i)-1))
for i in range(1,n+1):
    print('*'*(i))

#count the number divisible by 3 and 5 from 1 to 100:
div_by_3=0
div_by_5=0
div_by_both=0
by3=[]
by5=[]
by_3_5=[]
for i in range(1,101):
    if (i%5==0):
        div_by_5+=1
        by5.append(i)
    if (i%3==0):
        div_by_3+=1
        by3.append(i)
    if(i%5==0 and i%3==0):
        by_3_5.append(i)
        div_by_both+=1
print(by_3_5,"TOTAL: ",div_by_both)
print(by3,"TOTAL: ",div_by_3)
print(by5,"TOTAL: ",div_by_5)


#write aprogram to compute the sum of first 5 natural numbers:
a=0
for i in range(1,6):
    a+=i
print(a)

#read 10 input from keyboard and add it and find average:
numbers=[]
sum=0
print("Enter 10 number")
for i in range(1,11):
    a=int(input("enter your "+str(i)+" number"))
    numbers.append(a)
for i in numbers:
    sum+=i
average=sum/10
print(sum)
print(average)

#write program to display n natural number and print tgeir suma and aVERAGE:
n=int(input("enter a value: "))
a=[]
sum=0
for i in range(1,n+1):
    a.append(i)
print(a)
for i in a:
    sum+=i
print(sum)
print("average is",str(sum/n))

# write a program to find a cube of a number:
num=int(input())
for i in range(1, num+1):
    print("the number is ",str(i)," and the cube is ", str(i**3))

#Write a Python program to concatenate all the strings in a list using a for loop