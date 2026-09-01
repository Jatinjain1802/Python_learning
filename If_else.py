'''
*****if else**********
->it is a keyword in python.
-> if block is excuted whent he condition is true but if the conditon
is false then else block is excuted
->it is used when we have excetedly two possiblites or choices
-> either if will be excuted or else
Note:
-> esle is follwed by if block
-> else has no conditon to check.
-> either if or else can be excuted(bith block cannot be excuted at the same time)
-> sytax:
if (condtion{always in boolean}):
    |# if block |
    |           |
    |           |
    |           |
    |-----------|
else :
    |# else     |
    |  block    |
    |           |
    |           |
    |-----------|

flowchart: statement is true then if block is excuate
otherwise else is excuted
'''


a=int(input("Enter any number"))
if (a >=0):
    print("postive number")
else :
    print("negative number")


name=input("Enter any name")
if ("a" in name):
    print("chater found")
else :
    print("chater not found")
print("Second approch")
if (name.find("a")>0):
    print("chater found")
else :
    print("chater not found")


