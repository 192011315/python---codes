new_count=int(input("enter the no.of loaves purchased:"))
old_count=int(input("enter the no.of old loaves purchased:"))
rate_old=(185-(0.6*185))*old_count
rate_new=185*new_count
if(new_count<=0):
    print("enter real number")
elif(old_count<=0):
    print("enter the valid")
else:
    print("regular price:185")
    print("amount of new loaves:",rate_new)
    print("amount of old loaves:",rate_old)
    print("total amount:",rate_old+rate_new)
