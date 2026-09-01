'''
types of variables with respect to function scope:-
1) Local variable:- any vaiable which is delcred insde that
function . it can be only accessed only inside the funciton. they are
created insdie the funciton and after the function is completed
they are destroyed. parametrer are local varibale only
2) Global varibale:- declared outside of all funciton & function
global varibale can be accessed form anywhere in the module
u cannot modify global variable direclty

NOTE:- if the gobla and local have the same name then inside the
fucntion local will get priorty over the glovbal
'''

a=100

def display():
    global a
    b=90
    print("inside function before moify",a)
    a=a+60
    print("outside function",a)

display()
print("outside function",a)


a=20
def aa(a):
    a=50
    print(a)
aa(40)
print(a)
