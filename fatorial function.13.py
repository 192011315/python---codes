def factorial(n):
    if (n==1):
        return 1
    else:
        return (n*factorial(n-1))

num= int(input("enter a number:"))
if (num<0):
    print("doesn't exist !")
elif (num==0):
    print("0!= 1")
else:
    print("factorial of",num,'=',factorial(num))
    
