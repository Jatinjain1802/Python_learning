'''
ENCAPSULATION:- 
    -> Process of making data private and controlling their access throguh public setter and gretter methods
    -> Direct access IS NOT given to sensitive data,But the class shud control How the data is read/modified
    -> Step to achieve Encapsulation:
        1) A class should be public non abstract class
        2) Define Private variables
        3) Have public setter method (update data with validation logic) 
        4) Have Public getter method access.read data safetly
    syntax:- 
        class CLAssNAmr:
            def __init__(sel"
            
            def der_daw
            
---------------------------------------------
Achieving Encapsulation Using @property decoratore:-
    It is a way in python to access methods like variables 
    there are two type of Decoratore:-
    1) @property :- it is a decoratore allows method to behave like "getter". insted of calling it normally like a method. we can ACCESS it like a normal attribute. Ex:- print(instanceref.variable)
    2) @property.setter :- It is a decoratore define the "setter" for the same property. allow you to ASSIGN a vlaue like a variable, but indireclty it calls a method. Ex:- instanceref.variable=newvalue
    
    Syntax:- 
        class ClassName:
            def __init__(self):
            slef.__var=value
        
        @property 
        def var(self):
            return self.__var
        
        @var.setter
        def var(self,newvlaue):
            # logic
            self.__var=newvlaue
        
        obj=ClassName()
        print(obj.var)
        obj.var=value #initilise it liek a variable and the setter method gets called
        
    1) Getter MUST come first (besoz getter defines the property)
    2) Setter MUST come after the Getter (setter work on that)
    3) Always use same method name for both setter and getter and the property
        
'''

class Paient:
    def __init__(self,name,age,bp):
        self.name=name
        self._age=age
        self.__bp=bp
    
    def Check_up(self):
        return self.__bp
    def restore_bp(self,value):
        if value>=80 and value<=120:
            self.__bp=value
            print(self.Check_up())
        else:
            print("you are dead")

p1=Paient("jatin",23,95)

print(p1.Check_up())
p1.restore_bp(140)
# print(p1.Check_up())