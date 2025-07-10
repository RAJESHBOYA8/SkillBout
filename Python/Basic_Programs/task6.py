def average(marks):
    y=True
    for i in marks:
        if i>100 or i<0:
            y=False
            break
    return avg(marks) if y else "Marks are invalid"
def avg(marks):
    return sum(marks)/len(marks)

def grade(marks):
    if average(marks) >= 90:
        return "A"
    elif average(marks) >= 80:
        return "B"
    elif average(marks) >= 70:
        return "C"
    elif average(marks) >= 60:
        return "D"
    elif average(marks) >= 50:
        return "E"
    else:
        return "F"

name=input("Enter Student Name: ")
marks=list(map(int,input("Enter marks: ").split()))
print("The average of the marks is : ",average(marks))
print("The grade of the marks is : ",grade(marks))