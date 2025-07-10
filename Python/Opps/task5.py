class Employee:
    def display1(self):
        print("This iis Employee Class")
class Manager(Employee):
    def display(self):
        print("This is  Manager Class")
m=Manager()
m.display1()
m.display()