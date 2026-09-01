'''
we can place one if block of code inside another if block of code
this is used to check multiple level of condition
'''

mail=input("ENter the mail ID")
if mail=="test@gmail.com":
    password=input("enter the pass")
    if password=="12345":
        print("Login succesful")
    else:
        print("Wrong password")
else:
    print("Enter valid mail")
