'''
Opps depend on 2 concepts and 4 principles:-
    2 concepts:-
        a) Class
        b) Object
    4 Principles:-
        a) Encapsulation
        b) Inheritance
        c) Polymorphism
        d) Abstraction
        
----------------------------------------------
-> Object-Oriented:-
        -> Represent everything in the form of object that store data (states) and perform action (behaviour)
        -> Python treates almost everything as an object (number,str,list,func,etc)

-> Class:-
    ->Blueprint that describe the property and behaviour of an object
    ->class define  states repressetn using variable
    -> behaviours represent using method
    
    Syntax:- class ClassName:
             pass
             
-> Object :-
    ->Instance of a class
    -> real world entity or logical entitiy that has state and behaviour
    instantion-> process of creating instance of a class
    
    syntax:- Reference_variable=ClassName()
    
NOTE:- One class create many object

-------------------------------------------------------------------------------

# Memory Allocation wrt Class and Instance
    -> When class is define, class dictionary is created and inside it variable and methods of that class is stored in the form of key and values. to see this use this . ClassName.__dict__ 
    ->When instance (object) is created, instance(obj) dictionary gets created and inside it instance(obj) data is stored in the form of key and values, it will have a reference to class. to see this use this  objreference.__dict__  
    -> using same class:
        -> We can create multiple instance (object) and each instance(obj) is independent entity
        ->chnages made to 1 instance(object) DOES NOT affect other instances(obj)
    
NOTE:- print(ClassName.__dict__)   #get the class dictionary 
       print(objreference.__dict__)  # get the object dictionary 
       
1) class Variable:- 
        a) define inside a class but outside all methods
                syntax:- class ClassName:
                            variable_name=value
        b) outside the class, it can be define using the ClassName
                syntax:- ClassName,variablename=name
    -> only 1 copy of class varibale for entire class and it is not tied to any single intance
    -> if any value is common for all instance, it shud be made as classvariable
    -> how to access the class variable:-
        a) ClassName.variablename
        b) instanceref.variablename  
    -> modification of class variable will affect all the instance
        a) ClassName.variablename=newvalue 
    -> All class variable are store in class dictionary  

2) Instance variable:-
    -> varibale which are define using instance
    -> instance creation is compulsory to declare instance varibale
    -> syntx:-
            instance_referecne.varibale_name=value
    -> one copy for each instance, created seprately for each instance
    -> if a varibale is unique for that object , only then it as a instance varibale
    -> instance variable are stored inside instance dictionary 
    -> We can ACCESS and MODIFY an instance varibale
            assessing:- instanceref.varibalename
            modification:- instanceref.variablename=value
    -> modification will affect all spefic reference

-----------------------------------------------------------------------------------

Constructor/Initialiser->
    It is a block of code/specil dunder method used to declare and initialized insatance variable of an instance.it is used for instance varibale
    
    ->syntax: 
        class ClassName:
            def __init__(self):       #Initialiser/constructor
                slef.Variablename=value       # Initialising the Instance Variable
                    
        obj=ClassName()
    ->it should be alsoways made inside the class and its name should be `__init__(self)`
    ->self must be the first parameter in the constructore and it refer to the current invoking insatance
    -> Using Self parameter inside the constuctore we define Instance variables using 
    syntax:self.variablename=value
    -> instance creation is compulsary in order to execute initializer/constructor
    -> if their are n parameter in the constructore,we need to pass n-1 argumrnt during the instance creation/constructor call

Types of constructor:-
1) Default Constructor :-
    - it will not be visible to the user 
    - this will be present in the super class object
    - when the user does not provide custom constructor it is created
2) Custom constructore:-
    - will be define by user explicitly in the class
        2.1) Nonparamterised constructore:-
            - only having self as a paramter
            - used when we dont want to initialised the custom values
        2.2) Parameterised constructoe:- 
            - we give parameter
------------------------------------------------------------------------------------------
''' 
