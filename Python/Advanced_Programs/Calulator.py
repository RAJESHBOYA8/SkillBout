class Caluculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        try:
            c=self.a/self.b
            return c
        except ZeroDivisionError:
            print("You can't divide by zero")
#Driver code
a,b=map(int,input("Enter two numbers: ").split())
c=Caluculator(a,b)
print(c.addition())
print(c.subtraction())
print(c.multiplication())
print(c.division())


