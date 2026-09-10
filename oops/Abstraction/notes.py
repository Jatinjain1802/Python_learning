'''
Abstraction:-
    It is important Oops principle,which is the process of "defining required behaviours in parent class without providing full implementation and Forcing the subclass to implement it"
===========================
Abstract class(Incomplete Class):-
    -> It is a class that is meant ONLY for inheritance, becoz it CANNOT be Instantied (Object Creation is not possible)
    -> abstract class is a idea/concept and is incomplete by design
    -> should have atleast 1 "abstract method"
    NOTE: It acts like a contract , which ENFORCES the rules upon subclasses
---------------------------
abstract method-> 
    -> It is method declared in abstract class decorated using @abstractmethod
    -> is an incomplete method, having method name and parameter, BUT NO implementation
    -> it is meant to be overriden/implemented by the child classes
    syntax:- 
            form abc import ABC,abstractmethod
            class ClassName(ABC):
                @abstractmethod            #should have at least 1 abstraxct method decorsted with @abstractmethod.
                def methodname(self):
                    pass
    NOTE:- 
    abc:- abstract base classes, is a module in python used ot supprot abstraction
    ABC:- abstrsct base class, is a class imported from abc module, which is used as baseclass to create abstract classes
    @abstractmethod:- used to declare an abstract method and it is responsible to enforce abstraction
    
    Steps to make a class as an Abstract class 
        1) define a class that should inherit ABC class
        2) It shud contain Atleast 1 abstract method whcih shud be decorated using @abstractmethod
        3) abstract class CANNOT be Instantiated, we can create subclass instances using CONTRACT OF ABSTRACT
        4) CONTRACT OF ABSTRACT:- if a subclass inherits form abstract superclass, then the subclass MUST OVERRIDE all the abstract methods to create subclass instances or else the subclass will also become an abstract
---------------------------------------------
Application Programming Interface:=
- It acts as intermediate medium between 2 or more application
- It is a contract that define HOW a client CAN ACCESS a service without knowing how the sercive is implemented
- Abstract class helps us design such API contracts

========================
Tight Coupling:-
    If a change in serivce provider forces the user to make chnage in client side, then it is case of tight coupling 
    tight coupling is bad design principle becoz it expects the client code to chnaeg each time
    
'''
