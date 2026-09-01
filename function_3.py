# function with parameter and without return
def register(name,phonenumber):
    print("User registration sucessfull")
    print(f"Name:{name}\nPhonenumber:{phonenumber}")
#name=input("Enter your name")
#phonenumber=int(input("enter phone"))
register("name",987987908)

def send_otp(phonenumber):
     print("OTP Sent sucessfull")
     print(f"Phonenumber:{phonenumber}")
send_otp(98987098098)
    
# function with parameter and with return
def add(a,b):
    print("adding two number........")
    c=a+b
    return c
print(add(2,3))

def sub(a,b):
    print("subrating two number........")
    c=a-b
    return c
print(sub(2,3))

def mul(a,b):
    print("multipling two number........")
    c=a*b
    return c
print(mul(2,3))

def div(a,b):
    print("diving two number........")
    c=a/b
    return c
print(div(2,3))
