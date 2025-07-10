class Account:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__balance=0
    def setBalance(self,balance):
        self.__balance+=balance
    def getBalance(self):
        return self.__balance
acc=Account("John",100)
acc.setBalance(100)
print(acc.getBalance())