
#example:
i=0
while(i==0):
    print(i)
    i+=1
#print a number 1to5 using while loop
i=1
while(i<5):
    print(i)
    i+=1

# print a avlue btw 100 to 200:
i=10
while(i<=200):
    print(i,end=",")
    i+=10 

#print 1 to 10 in reverse order:
i=10
while(i>0):
    print(i, end=",")
    i-=1

#write program to find factorial
num=int(input())
fact=1
while(num>0):
    fact*=num
    num-=1
print(fact)