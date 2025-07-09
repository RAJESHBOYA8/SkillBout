def countwords(file):
    try:
        f=open(file,'r')
        words=f.read().split()
        count=len(words)
        f.close()
        return count
    except FileNotFoundError:
        return "File not found"
print(countwords("task4.txt"))