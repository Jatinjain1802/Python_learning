'''
1) positinal arguments:- values that are passed in the same order as the
parameters defined is know an psoitinal arguments.order matter and
count matter(No. of parameter = No. of arguments). it has a drawback that when
parameter are more then we cannot use it and also user should rember order
2) Keywords arguments:-values are passed during function call using Parameter names.
order does not matter in this case. count matter a lot

NOTE:- For the same parameter naem we cannot provide more then once.
key words 

3) variable lenght arguments:- used in function declaration when you don't
know how many arguments will be passed during the function call. 
    3.1) variable positinal argument(*args):- we use (*args) in function
    declation. which collect extra psoitional arguments into tuple.
    *args must come after all positional arguments. when we use
    *args in the function declation we can see packing concept in the
    function.
    when we use *iterable in the function call, we can see UNPACKING
    and it unpacks into psoitional arguments and make sure that the no. of
    parameter shud be equal to the no. of values unpackes
    3.2) variable keyword argument(**kwargs):- we use **kwargs in the
    function declation which collects extra keywords arguments into dictonary
    **kwargs can be used once
    **kwargs must come last in function declaration
    when we use **kargs in the function declation we can see packing concept in the
    function.it is packed in dictionary
    we can do unpacking into keyword arguments and make sure
    that the keyname which is unpacked should match the parameter
4) default argument:-it is a parameter in a fucntion declation
which already has a predfine vlaues
if user does not give the paramerter value then defualt vlaues are used
if we pass the value then the new vlaue will replace the old vlaue
'''
# Keywiords paramter ex
def sum (a,b):
    c=a-b
    return c
print(sum(b=6,a=9))
    

def sum(*args):
    sums=0
    for i in args:
        sums=sums+i
    print(sums)
sum(1,2,3,4,5)

l=[10,20,30]

def check(*a):
    print(a)
check(*l)
print("-------------variable keyword argument(**kwargs)------")
dic={"name":10,"jjj":20,"3":20,"4":40}

def check(**a):
    print(a)
check(name=10,jjj=20,ege=20,ee=40)

def unpacking(**dic):
    print(dic)
unpacking(**dic)

print("-------------Default------")
def minus(a=5,b=3):
    mins=a-b
    return mins
print("minus",minus())
print("minus",minus(10,20))
