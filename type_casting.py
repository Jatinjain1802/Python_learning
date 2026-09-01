'''
Type casting:- the process of converting one data type into another data type
is knon astype casting.
-> need of type casting"-
1) to store the vlaue in a particular manner 
2) match the data for a particular operation
3) to formate input/output


Types:-
1) Implicit typecasting:-
    ->Pyhtone automatically converts one data type into another during operation
    ->Usally seen when a smaller data type is promoted to bigger /larger datatype to avoid data loss
2) Explicit Type casting:-
    -> programmer manuallly convert one datatype into another using builtin function/class
    -> useful when python cannot decided or when we want a specific type
    
'''
print("====================single vlaue=========================")
print("=================Implicit typecasting=====================")
b=True
i=5
f=2.1
c=3+3j
print("-------------------bool-------------------")
b_i=b+i #  opreation between bool and int we get int
print(b_i)

b_f=b+f  # opreation between bool and float we get float
print(b_f)

b_c=b+c # opreation between book and complex we get complex
print(b_c)

print("-------------------int-------------------")
i_f=i+f  # opreation between int and float we get float
print(i_f)

i_c=i+c  # opreation between int and complex we get complex
print(i_c)


print("-------------------float-------------------")
f_c=f+c  # opreation between float and complex we get complex
print(f_c)
print("Ascending order")
print("bool>->int->float->complex")

print("====================Explicit typecasting ==============================")
b=True
i=5
f=2.1
c=3+3j
print("-------------------bool to int-------------------")
print(int(b))
print("-------------------bool to float-------------------")
print(float(b))
print("-------------------bool to complex-------------------")
print(complex(b))
print("-------------------float to int-------------------")
print(int(f))
print("-------------------complex to int -------------------")
#print(int(c)) # cannot convert complex to int
#print(float(c)) # cannot convert complex to in
print("====================Multi vlaue=========================")
l=[10,20,30]
t=(11,22,33)
s={21,22,23}
st="ABC"
d={1:100,2:200,3:300}
print("------list---------------")
print("-------------------list to tuple -------------------")
print(tuple(l))
print("-------------------list to set -------------------")
print(set(l))
print("-------------------list to str -------------------")
print(str(l))
print("-------------------list to dic -------------------")
#print(dict(l))  # because of key value

print("------tuple---------------")
print("-------------------tuple to list -------------------")
print(list(t))
print("-------------------tuple to set -------------------")
print(set(t))
print("-------------------tuple to str -------------------")
print(str(t))
print("-------------------tuple to dic -------------------")
#print(dict(t))  #print(dict(l))  # because of key value

print("------set ---------------")
print("-------------------set to list -------------------")
print(list(s))
print("-------------------set to tuple -------------------")
print(tuple(s))
print("-------------------set to str -------------------")
print(str(s))
print("-------------------set to dic -------------------")
#print(dict(t))  #print(dict(l))  # because of key value

print("-----------str ---------------------")
print("-------------------str to list -------------------")
print(list(st))
print("-------------------str to tuple -------------------")
print(tuple(st))
print("-------------------str to set -------------------")
print(set(st))
print("-------------------str to dic -------------------")
#print(dict(t))  #print(dict(l))  # because of key value

print("-------------dict --------------------")
print("-------------------dict to list -------------------")
print(list(d)) # list of key
print(list(d.values())) # list of value
print("-------------------dict to tuple -------------------")
print(tuple(d)) # tuple of key
print(tuple(d.values())) # tuple of value
print("-------------------dcit to set -------------------")
print(set(d)) # set of key
print(set(d.values())) # set of value
print("-------------------dcit to str -------------------")
print(str(d)) 

print("--------------int to str")
print(str(i))
print(type(str(i)))
print("--------------bool to str")
print(str(b))
print(type(str(b)))
print("--------------complex to str")
print(str(c))
print(type(str(c)))
print("--------------float to str")
print(str(f))
print(type(str(f)))

print("--------------list to bool")
print(bool(l))
print("--------------tuple to bool")
print(bool(t))
print("--------------set to bool")
print(bool(s))
print("--------------str to bool")
print(bool(st))
print("--------------dic to bool")
print(bool(d))

print("-----------collection to single data type (parsing) -----------------")

st="10"
print(int(st))
print(type(int(st)))

sf="2.1"
print(float(sf))
print(type(float(sf)))

sb="False"
print(sb)
print(bool(sb))
print(type(bool(sb)))


sc="3j"
print(sc)
print(complex(sc))
print(type(complex(sc)))

print("===========Question============")
dance=["jatin","heer"] 
singing=["heer","annu"]
player=["annu","manish"]
dance.extend(singing)
dance.extend(player)
'''
student=set(dance)
print(len(student))
print(student)
'''
students=set()
students.update(dance)
print(students)
print(len(students))
