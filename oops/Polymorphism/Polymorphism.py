'''
Polymorphsim:- 
-> It is the ability of the single interface to perform different action depending on the object it is appiled to
-> In pyhton. polymorphism allows same operatore or method to behave differently depending on the object

=> Polymorphism in implemented using 3 Ways:-
1) Method Overriding:- 
    ->It is a feature of inheretance where the child class provide its own implementation for a method that is already defined in its parents class using the same method name and signature
    -> steps :
        1.1) Inheritance
        1.2) Method name of parent class and child class must be same
        1.3) no. of paramater usually shud be same
        1.4) Implementation in the child method shud be chnaged
    -> syntax:- 
        class ParentClass:
            def methodname(self):
                #method implemented by parent
        class ChildClassName(ParentClass):
            def methodname(self):     #methodname shud be same as parentclass method
                #child method Implementation chnage
    -> example is in file1.py

------

Super()
-> it is a inbuilt fucntion that allows a child class to call form parent class.proper way of accessing parents class
syntx:- super().methodname(args). 
        if parent class have 'n' parametert thne 'n-1' args
        
"constructor chaining":-
    It is the process where in parent class constrcutor is invoked/called from child class constructor using super().
    Note:-
        1) Defining a constructor (__init__) in a chile class will STOP the parent class constructore form being automaticlay called. The parents class attribuites won't be initialized unless you "explicitly call"
            super().__init__() form the constructor.
        2) Super() doesn't just call the immediate parent-it follows the "Method Resolution Order (MRO)" in inheritance hierarchies,espically important in multiple inheritance
    syntax:-
        class Parent():
            def __init__(self):
                parnet logic
        class child(Parent):
            def __init__(self):
                super().__init__()
                child logic
        obj=child()
----------
2) Operator Overloading:-
    Operator overloading is the ability to chnage the behaviour of an operatior. so that it work objects of user define classes. This is done by defining special method often called "dunder".
        1) Arthimatic dunder method:- 
            used to define the behaviour for mathematical operators like +,-,*,/
            when you use operatore , python calls corresponsding dunder method on the object on the left side
            These must return new object
            they atr not deifne 
    
    Operator               Dunder Method            expression          method call
    +                     __add__(self,other)        a+b                a.__add__(b)
    -                     __sub__(self,other)        a-b                a.__sub__(b)
    *                     __mul__(self,other)        a*b                a.__mul__(b)
    /                     __truediv__(self,other)    a/b                a.__truediv__(b)
    **                    __pow__(self,other)         a**b               a.__pow__(b)
    //                    __floordiv__(self,other)    a//b             a.__floordiv__(b)
-----------------------------------
2) relational duner methods :- 

    used to define the behaviour for relational operators like <,>,<=,>=,==,!=
    when you use operatore , python calls corresponsding dunder method on the object on the left side
    These must return boolean value
    
    Operator               Dunder Method            expression          method call
    <                     __lt__(self,other)        a<b                a.__lt__(b)
    >                     __gt__(self,other)        a>b                a.__gt__(b)
    <=                    __le__(self,other)        a<=b               a.__le__(b)
    >=                    __ge__(self,other)        a>=b               a.__ge__(b)
    ==                    __eq__(self,other)        a==b               a.__eq__(b)
    !=                    __ne__(self,other)        a!=b               a.__ne__(b)
------------------------------------------
3) Ducktyping:-
    Duck typing is a programming style which does not look at the type of object but at the methods and properties of the object. If it looks like a duck and quacks like a duck, then it must be a duck.The name comes form the saying "If it looks like a duck and quacks like a duck, then it must be a duck."
    
    In python this means
        -> If an object implements certain methods and properties, it can be used in a context that expects those methods and properties, regardless of the object's actual type.
        -> python "focused on behavior" rather than "type"
        -> Example:- ducktyping.py
    
    --> hasattr() function:-
        -> it is used to check if an object has a particular attribute or method. It returns True if the object has the attribute, and False otherwise.
        -> It return the boolean value.
        -> used to get safe duck typing. It is used to check if the object has the method or not before calling it.
'''
