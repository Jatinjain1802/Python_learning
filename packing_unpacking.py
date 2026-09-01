'''
packing:- colleting/grouping multiple vlaues in to single collection
        - pyhton by default pack thing in tuple if we do not specifiy
    *types:
    1) Manual/explicit Packing:- user decided the colletion type like list,set,dictnoary,tuple
    2) Implicit packing:- user does NOT specify the collection type,pyhton
    will automatically packs the values into tuple
sytnx:
Variable name=v1,v2,v3,v4,v5 # by default it is implicit packing
-------------------------
unpacking:- Extracting the values from a sequence and assigning them
into individual variables
rules of unpacking:-
    1) if their are n vlaues in a collection we need to have n variable
    during unpacking UNLESS we use * for leftovers
    2) Extended iterable unpacking - when we do not know the number of vlaues to
    unpack. we use * valriable in the left hand side. which collect the remaing vlaues
    in the list formate
        2.1) only one star(*) should use during assigement
        2.2) we can use star valribale to the left,right,center
        2.3) it collect in list 

'''
p=10,20,30,40,50,60,60
print(p)
print(type(p))

l=[10,20,30,40,76,890,76,4,46464,64,6464,64,64,67,45,4,54,4,64,64,6,46,4]
a,*b,c=l
print(a,b,c)
