'''
Decorators:- iT IS A FUNCTION modifies the behavior of
another function wihtout chnaging its code.
-It takes another dunciton as input
-adds estra behaviour
-retrun new function

used for resuablit

setps to create a decorators:-
    1) define nested funciton
    2) outer funciton shud take 1 parameter whihc accepts a function
    passed as argumanet
    3) Decorators logic should be inside the inner fucntion
    4) the outer function should return the inner fucntion

NOTE:-
1) The outer function name usally can be named as decoratores and
inner fucntion can be named as wrapper
2) the no. of parameter in the function to be decorated must be
same with the inner/wrapper fucntion
'''
'''
gift_name=input("Enter the name of gift")
def decorators(function):       #decoratore wiht the paraper fucntion to be decorated
    def wrapper():          #inner function where the funciton will be decoration will done
        print("Take a gift paper")
        function()
        print("Place the lable to it")
    return wrapper

def gift():      #fucntion which is to be decorated
    print(f"{gift_name} is slected")
gift()
print("======decoration begin=======")
gift=decorators(gift)
gift()
'''
#cake_name=input("Enter the name of cake")
def decoratoros(function):
    def wrapper(*args,**kwargs):
        print("slect the cream")
        function(*args,**kwargs)
        print("put the candles and cut it")
    return wrapper
def baked_cake(*args,**kwargs):
    print("cake is slected\n",args ,kwargs)
baked_cake=decoratoros(baked_cake)  # manual decoratore
baked_cake()


def decoratoro(function):
    def wrapperr(*args,**kwargs):
        print("slect the cream")
        function(*args,**kwargs)
        print("put the candles and cut it")
    return wrapperr
@decoratoro      # automatic decoratore
def gift(*args,**kwargs):
    print("toy car",args ,kwargs)
gift("lego","BMW m4", typee="BMW",price=4500)
