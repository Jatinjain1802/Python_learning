'''
Generator:- It is used ot create the coustom sequnece of element
using the "yield" keyword.

-> it a user-define function contians at least one yield keyword,
    then that function becomes a generator function
-> Generators generates value one by one
-> Mainly used ot create the sequnece (like even number,odd,number
    fibonacci,prime,infinite sequences,large data stream)


NOTE:- return stops the funcniton but yield pause the fucntion

    1) returns the yield value to the caller
    2) pause the function
    3) when you call next() it will resumes right after yield
    4) automatically creat the iterator

Syntax:- def function():
            FUNCTION BODY
            yield value
         gen_obj=function()

'''

def fun():     #1) generatore object
    print("hi")
    yield 10
    yield 20
    yield 30
    yield 40

gen_obj=fun()  #2) generatore fyunmction is created
print(gen_obj)

print(next(gen_obj))
print(next(gen_obj))   

print(next(gen_obj))   

print(next(gen_obj))   



def sequence():
    value="*"
    space=" "
    yield f"{space*0}{value*10}"
    yield f"{space*2}{value*5}"
    yield f"{space*4}{value*1}"
    yield f"{space*2}{value*5}"
    yield f"{space*0}{value*10}"

genn_obj=sequence()
print(next(genn_obj))
print(next(genn_obj))   

print(next(genn_obj))   

print(next(genn_obj))
print(next(genn_obj)) 


