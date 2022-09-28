ba=int(input("Enter starting :"))
b=int(input("Enter end :"))
c=int(input("Numbers to skip:"))
d=a
while(a>0):
    if(d<b):
        print("Skipeed numbers :",d)
        d=d+(c+1)
    else:
        break
