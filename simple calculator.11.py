def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print("enter a choice:")
print("1.addition)")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter choice 1/2/3/4:")
    if choice in ('1','2','3','4',):
        x=float (input("enter the first number:"))
        y=float (input("enter the second number:"))
        if(choice=='1'):
            print('addition',add(x,y))
        elif(choice=='2'):
            print('sub',sub(x,y))
        elif(choice=='3'):
            print('mul',mul(x,y))
        elif(choice=='4'):
            print('div',div(x,y))
    else:
        print('the operation does not exist!')
        
        
     
