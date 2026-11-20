'''
Method:- ANy function which is deifne insdie the class

1) Class Method:- 
    -> it belong to class itself , not the instance
    -> works on class level data not the instance
    -> recevie the class reference as the parameter to cls
    -> it is declared using `@classmethod` decoratore just above the method
    -> syntax:- class ClassName:
                @classnethod
                def method_name(cls,para1,para2):
                    #method body/logic
    -> if their are "n" parameter are their then we have to pass "n-1" arguments during the class method calling
    -> A class method can ACCESS and MODIFY the class variables
    -> accessing the classsmethod using ClassName.classmethod()
2) Innstance Method :- 
    -> it belong to insatnce
    -> it work on instance spefic data
    -> recevie the current instance reference as the 1st parameter reffrend to self
    -> syntax:  class ClassName:
                    def method_name(self,para1,para2.....):
                    @mothod/logic
                reference=ClassName()
                refernce.method_name(arg1,arg2,....)
    -> if their are "n" parameter are their then we have to pass "n-1" arguments during the instance method calling
    -> A instance method can ACCESS and MODIFY the instnce variables
    -> accesgign is doen by instancemethodname()
               
3) static Method :-
    -> Do not depend on class or instance
    -> does not operate on class or insatnce data
    -> DOES NOT receive self or cls as the 1st paramter
    -> shud be define using `@staticmethod` decoratover above that
    -> syntx:-
        class ClassName:
        @staticmethod
        def method_name(para1,para2,para3):
            logic
    -> callin it by class:- ClassName.method_name(arg1,arg2,........)
    -> callin it by instace:- instanceref.method_name(arg1,arg2,........)
    -> if "n" paramter are presnet in the static method, then n argument should be pass
    -> it can be call or invok by both class or object(instance)
    -> behave like a normal function, but it is a logic which is realted to class -> knwon as helper class utiltiy method

## Importance of MEhtod:-
    1) enforce a logic before data
    2) AAvoid code duplicatio
    3) Adheres principles of OOPs
    4) It allows abstraction
'''