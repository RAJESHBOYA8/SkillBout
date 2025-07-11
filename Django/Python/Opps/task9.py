#abstraction
from abc import ABC, abstractmethod
class Paymentmethod:
    @abstractmethod
    def pay(self):
        pass

class UPI(Paymentmethod):
    def pay(self,amount):
        return amount*100
upi=UPI()
print(upi.pay(100))
