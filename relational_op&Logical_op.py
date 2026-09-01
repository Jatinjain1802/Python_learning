'''
This opreatore are used to compare the vlaue/variables.
The output is always in the boolean form

== Comparisin
> greater than
>= greater than or equal to
< lesser then
<= lesser then or equal to
!= not euqal to

'''
a=10
b=4
print(a>=b)
print(a<b)
print(a<=b)
print(b==4.3)
print(b!=4.3)
print("--------Logical Operators----------")
'''
Logical Operators:-
This opreatore are used to evaluate conditions or combine condition
-> and,or,not are the logicla operatore
-> they usually return boolean values

'''
print("======and========")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# if it get the truthly vlaue at first position it reutn the other vlaue and if it get the falsey vlaue at the first place then it stop and it return the first vlaue only
print(5 and 4)
print (5 and 0)
print (0.0 and 5.4)
print ([] and "Hi")
print ("0" and "0.0")
print("======or========")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# if it get the truthly vlaue at the first it reutn the first vlaue and if it get the falsey vlaue at the first place then it stop and it return the second vlaue only

print({} or set())
print (5 or {})
print (0.0 or 5.4)
print ([] or "Hi")
print ("0" or "0.0")

print("======not========")
print(not True)
print(not False)




