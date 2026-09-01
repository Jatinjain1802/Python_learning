'''
Lambda function:- it is a small function defining using lamda
keyword. it is written in single line and used ofr short orpeation
A function whihc does nto have a name. 
NOTE: It is best when we need ot pass simple helper function for
higher order function(whihc takes other fucntion as a pararameter)

sytanx :-
        lambda argunents: expression
Rules:-
    1) No funciton name
    2) No return keyword
    3) Expression result is returned automatically
    4) Only ONE expression is allowed

Example:-
1) ADD FUCNTION
NORMAL FUCNTION:
    def add (a,b):
        return a+b
In lambda funtion:-
    lambda a,b:a+b
1) MULTIPLY FUCNTION
NORMAL FUCNTION:
    def mul (a,b):
        return a*b
In lambda funtion:-
    lambda a,b:a*b


CALLING OF LAMBDA FUNCITON
1) Assign to variable
2) direct call
'''
from functools import reduce
add=lambda a,b:a+b # assign to variable
print(add(2,3))

print((lambda e,f,g : e*f*g) (2,3,4))   # direct call
ADD= (lambda e,f,g : e+f+g) (2,3,4)  # direct call
print(ADD)
l=[10,20,30,40,50]
def square(num):
    return num**2

def transfrom (fun,col):
    square_list=[]
    for i in col:
        result=fun(i)
        square_list.append(result)
    return square_list

print()
print(transfrom(square,l))
# by lambda fucntion
print(transfrom(lambda num:num**2,l))
def transfromm (col):
    square_list=[]
    for i in col:
        result=(lambda num:num**2)(i)
        square_list.append(result)
    return square_list
print(transfromm(l))
'''
IMPORTANT PREDEFINE HIGHER ORDER FUCNTION:-
1) map():- applies a given function to each item in an iterable.
    return a map object(an iterator). yeah aapn use krte hai jb
    aapne ko ahr element ko itrate krna hota hai.
    after the excuation the the map object get empty
    in this if oyu use labda fucntion we cannot have moe then one
    paramter
syntx:- map(function,iterable)
        -function:- shud takes one arguments and return one value
        -iterable - sequence (list,tuple,etc)
2) filter():- filter out the elements from an itreable based on a
    certain condition. return the filter object. it filter only those
    element where function return true and adds it to filter object
syntax:- filter(funciton,iterable)
        -function:- this function passed as an parameter. must take
        one parameter and must return true or false.
        -iterable:- sequence (list,tuple,etc)
3) reduce():- it is fucntion from functools module(from functools
    import reduce)
    It applies a function cumulatively to the items of iterable,
    reducing them to single vlaue
syntax:- form functools import reduce
         reduce(fucntion,iterable)
         -function:- funcntion that takes two argumaents and shud
         return a singlevalue.
        -iterable:- sequence (list,tuple,etc)
'''

print("----------map()----------------------")
root=map(lambda num:num**2,l)
print(list(root))
# get empty
print(root)  
print(list(root))
print(list(map(lambda num:num//5,l)))
print("----------filter()----------------------")
even=filter(lambda a:a>30 and a<50,[11,22,33,44,55])
print(list(even))
# get empty
print(list(even))
print("----------reduce()----------------------")
add=reduce(lambda a,b:a+b,[11,22,33,44,55])
print(add)
mul=reduce(lambda a,b:a*b,[1,2,3,4,5])
print(mul)
print("----------Question----------------------")
square=map(lambda num:num**2,[10,12,13,14,16,17,18])
square=list(square) # storing the list in square for future use
print("Square no.->",square)
even=filter(lambda num:num%2==0,square)
print("even square no.->",list(even))
print("sum no.->",reduce(lambda a,b:a+b,square))
