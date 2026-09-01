'''
Function which is define inside another function is called a
nested function.
syntax:

def outer_fun_name():
    def inner_fun_name():
        pass

->inner function is only accessible within/inside the outer function
implementation, unless it is return.
-> We use nested fucntion when one funciton helps another function
but we don't want it to be used outside
-> like a helper funtion but private for main function

NOTE:-
Enclosing varibale define inside the outside function and accessed
inside the nested/inner function is called enclosing variable
inner function can assess the outer fucntion variable
if we try to modify varibale of the outer funtion inside the
inner function we get unbounderror. we use "nonlocal"
keyword inside the nested funciton
'''

'''
A=100
def outer():
    b=200
    print("outer function")
    print(A)
    print(b)
    def inner():
        print("inner funtion")
        print(A)
        print(b)
    return inner
a=outer()
a()
'''
'''
def outer():
    a=100
    a=a+50
    def inner():
        nonlocal a
        print("inner function")
        a=a-20
        print(a)
    print(a)
    inner()
outer()

'''
b=int(input("enter the time you want the counter"))
def counter():
    count=0
    def incremnt():
        nonlocal count
        count=count+1
        print(count)
    for i in range(0,b):
        incremnt()
    
counter()


