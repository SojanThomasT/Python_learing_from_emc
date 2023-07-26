class company():
    def __init__(self):
        self.__companyname="Google" #private cannot access outside the box
        self._companylogo="google doggle"
    def company_name(self):
        print(self.__companyname)
        print(self._companylogo)

c1=company()
c1.company_name()    # print output
print(c1._companylogo)  #print logo
print(c1.__companyname) #error will come