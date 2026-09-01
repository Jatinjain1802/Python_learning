'''
Mactch case was introduce in python 3.10 and it is python version of
switch.
-> it matches the structure and vlaues and the mathcing case block excuted
'''
num=int(input("ENter the day"))
match num:
    case 1:
        print("MONDAY")
    case 2:
        print("Tuesday")
    case 3:
        print("Wenasday")
    case 4:
        print("thursday")
    case 5:
        print("Firday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Enter valid Day")

