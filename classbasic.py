class goa:
    name = "hii"
    drink = ""

    def party(self):
        print("Lets Party....!")
    def beach(self):
        print("Lets Swim")

#defining object
ramesh = goa()
suresh = goa()
#setting name and drink option:
ramesh.name="Ramesh" 
suresh.name="Suresh"

ramesh.drink="Yes"
suresh.drink="No"
print(ramesh.name," drink: ",ramesh.drink)
print(suresh.name," drink: ",suresh.drink)

class laptop:
    price=""
    processor=""
    ram=""

#defining object
HP=laptop()
DELL=laptop()
LENOVO=laptop()

#DEFINING OBJECTT
HP.price=500000
HP.processor="i5"
HP.ram="8Gb"

DELL.price=600000
DELL.processor="Core i3-12th Gen"
DELL.ram="16Gb"

print(HP.price)
print(DELL.price)