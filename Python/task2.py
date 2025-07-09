def reverseorder(l):
    low,high=0,len(l)-1
    while low<high:
        l[low],l[high]=l[high],l[low]
        low+=1
        high-=1
    return l
def summ(l):
    s=0
    for i in l:
        s+=i
    return s
def average(l):
    sum1=summ(l)
    avg=sum1/len(l)
    return avg

n=int(input("Enter a number: "))
l=list(map(int,input("Enter Numbers for the list ").split()))
print("The reverse order of list: ",reverseorder(l))
print("Sum of numbers in list : ",summ(l))
print("Average of numbers in list: ",average(l))