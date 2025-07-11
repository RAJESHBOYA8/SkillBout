class Demo:
    def __init__(self,a=None,b=None,c=None):
        if a and b and c:
            print("3 Args")
        elif a and b:
            print("2 Args")
        elif a :
            print("1 Args")
        else:
            print("No args")
Demo(1,2,3)
Demo(1,2)
Demo(1)
Demo()