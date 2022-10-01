print("Enter Two Numbers: ")
numOne = int(input())
numTwo = int(input())

if numOne>numTwo:
    lcm = numOne
else:
    lcm = numTwo

while True:
    if lcm%numOne==0 and lcm%numTwo==0:
        break
    else:
        lcm = lcm + 1

print("\nLCM =", lcm)
if numOne>numTwo:
    hcf = numOne
else:
    hcf = numTwo

while True:
    if numOne%hcf==0 and numTwo%hcf==0:
        break
    else:
        hcf = hcf - 1

print("\nHCF=", hcf)
