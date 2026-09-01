'''
Inheritance->
    -> It is the process of 1 class acquiring the properties of another class
    -> the class which shares the properties: parent or super or base class
    -> the class which acquires the rpopeties -> chlid or sub or derived class
    -> it can be reffered as "IS -A- Relationship"
    -> python we can inherit variables and methods
    
##types of inheritance:-
1) Single Inheritance:- 
    -> combination of 1 superclass and 1 subclass
    -> syntax:-
        class ParentClass:
            #class body
            #class methods and class veriable
        class ChildClass(ParentClass):
            #class body
    -> The method resolution order (MRO):
        > method order in which python Searches Classes to find that method
        > this is relevant only when there is more than 1 inheritance path
        > ClassName.__mro__
    -> example in file1.py
2) Multilevel Inheritance:-
    -> combination of 3 or more classes in a sequence
    -> syntax:-
        class GrandParentClass:
            #class body
        class ParentClass(GrandParentClass):
            #class body
        class ChildClass(ParentClass):
            #class body
    -> example in file2.py

3) Hierarchical Inheritance:-
    -> combination of 1 superclass and multiple subclasses
    -> syntax:-
        class ParentClass:
            #class body
        class ChildClass1(ParentClass):
            #class body
        class ChildClass2(ParentClass):
            #class body
    -> example in file3.py
    
4) Multiple Inheritance:-
    -> combination of 2 or more superclasses and 1 subclass in sequential manner
    -> syntax:-
        class ParentClass1:
            #class body
        class ParentClass2:
            #class body
        class ChildClass(ParentClass1, ParentClass2):
            #class body
    -> example in file4.py
    -> if both superclass have a same attribute name or method name,based upon mro the method present in the immediate superclass will be excuted
5) Hybrid Inheritance:-
    -> combination of 2 or more types of inheritance
    -> syntax:-
        # This is a combination of different types of inheritance
'''
