class Employee:
    #constructors
    def __init__(self):
        self.__name=name
        self.__salary=0
        self.__age=age
    def setname(self,name):
        self.__name=name
    def setsalary(self,salary):
        self.__salary=salary
    def setage(self,age):
        self.__age=age
    def getname(self):
        return self.__name
    def getsalary(self):
        if salary<0:
            print("salarymust br greater than zero")
        else:
            return self.__salary
    def getage(self):
        if age<18 or age>100:
            print("age must be between 18 and 100")
        else:
            return self.__age
#Driver code
name=input("Enter a name: ")
age=int(input("Enter age: "))
salary=float(input("Enter salary: "))
e=Employee()
e.setname(name)
e.setsalary(salary)
e.setage(age)
print("Name: ",e.getname())
print("Salary:",e.getsalary())
print("age:",e.getage())

