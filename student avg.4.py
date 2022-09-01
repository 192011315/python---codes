s1=int(input("enter the marks of s1:"))
s2=int(input("enter the marks of s2:"))
s3=int(input("enter the marks of s3:"))
avg=(s1+s2+s3)/100
if(avg>=90):
    print("grade A")
elif(avg>=80):
    print("grade B")
elif(avg>=70):
    print("grade C")
elif(avg>=60):        
    print("grade D")
else:
    print("grade F")
