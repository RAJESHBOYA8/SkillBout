from abc import ABC , abstractmethod
class Applience(ABC):
    @abstractmethod
    def turned_on(self):
        pass
class WashingMachine(Applience):
    def turned_on(self):
        print("turned on Washing Machine")
class Fridge(Applience):
    def turned_on(self):
        print("turned on Fridge")
app = WashingMachine()
app.turned_on()
fridge = Fridge()
fridge.turned_on()
