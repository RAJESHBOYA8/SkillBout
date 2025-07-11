def  divide(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return "Zero division Error"
a,b=map(int,input("Enter two numbers: ").split())
print(divide(a,b))

