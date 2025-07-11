class Marks:
    def __init__(self):
        self.__math_Marks=0
    def setMarks(self,math_Marks):
        self.__math_Marks+=math_Marks
    def getMarks(self):
        return self.__math_Marks
marks=Marks()
marks.setMarks(50)
print(marks.getMarks())