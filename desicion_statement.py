'''
desicion control statement-> This are used to control the flow of program
excution based on conditions
-> they allow the program to decide what to do dependeing on True/False
condition

types

1) if
-> it is a keyword in python and it excutes the block of code only when the condition
is true
-> this is used when we want to check or test the one conditon itself
-> sytax:
if (condtion{always in boolean}):
    |# if block |
    |           |
    |           |
    |           |
    |-----------|

flowchart: statement is true then if block is excuate otherwise end

2) if else
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

3) if elif else
4) match case
5) nested if


notes: Python is indentation language. it means providing or giving spaces
at the beginning of the line which is one tab space. it is mandaotry in python
for defining any block of code
'''
a=int(input("Enter any number"))
if (a >=0):
    print("postive number")
else :
    print("negative number")

name=input("Enter any name")
if (name.lower()=="gunda"):
    print("gunda found")
else :
    print(f"{name} found")

print("--------if_else---in new file------")










