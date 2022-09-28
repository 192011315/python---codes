a=int(input("Enter length of list1:"))
c=[]
for i in range(a):
    e=int(input("Enter element 1:"))
    c.append(e)
b=int(input("Enter length of list2:"))
d=[]
g=[]
for i in range(b):
    f=int(input("Enter element 2:"))
    d.append(f)
g=c+d
print("MERGED LIST :",sorted(g))
