'''
clouser
'''
'''
def outer ():
    a=100
    def inner():
        print("inner funcitonlaity")
        print(a)
    return inner
inside=outer()
inside()
'''

#b=int(input("enter the time you want the counter"))
def counter():
    count=0
    def incremnt():
        nonlocal count
        count=count+1
        print(count)
    return incremnt
    
count=counter()
count()
count()
count()

