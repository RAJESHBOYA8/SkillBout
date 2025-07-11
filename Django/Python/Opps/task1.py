class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name,self.price)
product1=Product("Cake",200)
product1.display()
product2=Product("Ice Cream",50)
product2.display()
