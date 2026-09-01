# 2. Input 2 numbers and print the larger number.

fnum=float(input("Enter first number"))
snum=float(input("Enter second number"))

if fnum>=snum:
    print(f"{fnum} is largest")
else:
    print(f"{snum} is largest")
    
    # 3. Take a dictionary of 4 items ,key shud be int and values shud be string and print only values associated with even keys
    
dic={1:"jatin",2:"heer",4:"manihs",5:"jstin",6:"sneha"}
for k,v in dic.items():
    if(k%2==0):
        print(k,v)