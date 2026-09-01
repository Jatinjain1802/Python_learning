# 1. Take a number input and print whether it’s positive, negative, or zero.
num=int(input("enter the number"))
if num>0:
    print("it is positinve")
elif num==0:
    print("it is Zero")
else:
    print("it is negative")
    
    
# 2. Input 2 numbers and print the larger number.

fnum=int(input("Enter first number"))
snum=int(input("Enter second number"))

if fnum>=snum:
    print(f"{fnum} is largest")
else:
    print(f"{snum} is largest")