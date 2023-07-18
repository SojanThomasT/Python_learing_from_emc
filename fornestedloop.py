
#week 1 and week 2 day i day 2
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
for i in (1,5):
    print("week ",str(i))
    for j in days:
        print("today is ", str(j))
    print("------------------------------")

#star pattern
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end=" ")
    print(" ")