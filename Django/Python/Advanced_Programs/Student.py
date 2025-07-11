class Student:
    #Constructor
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    #setting the Name
    def setname(self,name):
        self.__name=name
    #get the name
    def setmarks(self,marks):
        self.__marks=marks
    def getname(self):
        return self.__name
    def getmarks(self):
        if marks>0 and marks<100:
            return self.__marks
        else:
            print("Invalid marks")
            n=int(input("Enter the valid marks"))
            return n
#Driver code
name,marks=input("Enter a name and marks ").split()
marks=int(marks) #Converting marks from string to integer
s=Student(name,marks)#Assinging the object to the class
print(s.getname())#calling the getname method from Student class
print(s.getmarks())#calling the setname method from Student class
