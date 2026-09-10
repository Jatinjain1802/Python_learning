'''
EXCEPTION:-  Any unwanted or unexpected event that occurs during the execution of a program is called as EXCEPTION. It may be caused due to End User Input, Programming logic, Memory Problems etc.

In any programming language , there are two type of errors possible , they are,
1) Syntax error :- Error that occur because of INVALID syntax. The Programer is responsible to rectify these suntax error . Once all syntax error are corrected only then program execution will be started.

2) Runtime Error :-  While excuation of the program, if something goes wrong then we term it as Runtime errors and they maybe be caused due to 
            -> End User Input
            -> Programming logic
            -> Memory Problems
    -> such type of errors are called as EXCEPTION
NOTE: Exception handling is applicable for runtime Errors but not for Syntax Errors

===================================
Exception Handling in Python:-
It DOES not mean reparing or correcting the error but it means to handle the error in such a way that program execution will not be stopped and it will continue to execute the next statements.. Define a WAY, so that program DOES NOT Terminate abnormally and it will continue to execute the next statements.
-> MAin Approch of Exception handling is that it should not terminate the program abnormally and it should continue to execute the next statements.

Syntax of Exception Handling in Python:-
try:
    # Statements which may cause exception
    # Code which may cause exception
except ExceptionType:
    # ExceptionType is the type of exception which we want to handle
    # Statements to handle the exception
-------------------------------
Working of Exception Handling in Python:-
1) First the statements inside the try block will be executed.
2) If there is no exception then except block will be skipped and program execution will continue to execute the next statements.
3) If there is an exception then except block will be executed and program execution will continue to execute the next statements.
--------------------------------------------------
Exception Hierarchy in Python:-
   $ Base Exception
        |
        |---> SystemExit
        |---> KeyboardInterrupt
        |---> GeneratorExit
        |---> Exception
                |
                |---> StopIteration
                |---> ArithmeticError
                |       |
                |       |---> FloatingPointError
                |       |---> OverflowError
                |       |---> ZeroDivisionError
                |
                |---> NameError
                |---> AttributeError
                |---> ValueError
                |---> TypeError
                |---> EOFError
                |---> OSError
                |       |----> FileNotFoundError
                |       |----> PermissionError
                |---> ImportError
                |       |
                |       |---> ModuleNotFoundError
                |
                |---> LookupError
                        |
                        |---> IndexError
                        |---> KeyError
-------------------------------------------------------------------
DEFAULT EXCEPTION HANDLING IN PYTHON:-
1) For every exception type,a corresponding class is avaible and every exception is an object, so whenever an exception occurs, an object of that class is created and it is passed to the except block. If the Particular HANDLING CODE is NOT availabe, then python interpreter terminate the program abnormally and it will display the error message on the console.
----------------------------
Case 2) Exception shud occur only in try block .Only the code inside the try block will be checked for the excerption and its handling code. But, if there is any exception for the code before the try block, then abnormal termination.
-------------------------------------------------
Case 3) When no specific exception name is handled in except block, if you give wrong exception type in except block, then it will not handle the exception and program will terminate abnormally.
---------------------------------------
Case 4) Skipping below lines inside try block after exception occurs, if there is any exception occurs in the try block, then the remaining statements inside the try block will be skipped and control will be transferred to except block.
------------------------------------
case 5) what if exception occur at except block itself.abnormal ternimation. If an exception is raised inside the try block the execution goes to the except block . if the code inside the except block also raise an exception then it leadds to abnormal termination.
------------------------------------
case 6) What if exception occurs in the code after except block, then abnormal termination. If an exception is raised inside the try block and it is handled by the except block, then the control will be transferred to the next statement after except block. If there is any exception occurs in the code after except block, then it leads to abnormal termination.
================================
Approch 2 => In the exception handling code, we are printing our coustom message like "Exception passed" etc. Rather than that, we can also print exception information by creating a reference to the exception.
sytax:- 
        try:
            # Statements which may cause exception
            # Code which may cause exception
        except ExceptionType as ref:
            # ExceptionType is the type of exception which we want to handle
            # ref is the reference to the exception object
            # Statements to handle the exception
            print(ref)  # This will print the exception information
================================================
Approch 3 => Sometimes there may be a possibility that a piece of code can raise differnet exception in different cases.
-> in such cases in order to handle all exception we can use except block, so for every exception type we can write a separate except block to handle that particular exception.
-> syntax:-
        try:
            # Statements which may cause exception
            # Code which may cause exception
        except ExceptionType1 as ref1:
            # ExceptionType1 is the type of exception which we want to handle
            # ref1 is the reference to the exception object
            # Statements to handle the exception
        except ExceptionType2 as ref2:
            # ExceptionType2 is the type of exception which we want to handle
            # ref2 is the reference to the exception object
            # Statements to handle the exception
        except ExceptionType3 as ref3:
            # ExceptionType3 is the type of exception which we want to handle
            # ref3 is the reference to the exception object
            # Statements to handle the exception
==============================
Approch 4=> Instead of having multiple except blocks defined, we can have a single except block to handle all the exception types. In such cases we can use Exception class to handle all the exception types.
-> only things is that we will no thave the flexibility of customizing the message for each exception type. We can only print the exception information.
-> syntax:-
        try:
            # Statements which may cause exception
            # Code which may cause exception
        except (Exception1, Exception2, Exception3) as ref:
            # Exception is the base class for all the exception types
            # ref is the reference to the exception object
            # Statements to handle the exception
            print(ref)  # This will print the exception information
====================================
Default Exception Handling in Python:-We can use default except block to handling any type of exception,especially when we do NOT have ANY idea of which exception a particular code may raise.
-> When we have multiple except block, in that situation the default block is expected to be at the last.
-> syntax:-
        try:
            # Statements which may cause exception
            # Code which may cause exception
        except (ExceptionType1, ExceptionType2, ExceptionType3) as ref1:
            # ExceptionType1 is the type of exception which we want to handle
            # ref1 is the reference to the exception object
            # Statements to handle the exception
        except Exception as ref2:
            # This block will handle any type of exception which is not handled by above except blocks.
            print("Exception occurred")
====================================================
try,except,else and finally block in Python:-
1) try block:- The code which may cause exception is written inside the try block.
2) except block:- The code which will handle the exception is written inside the except block.
3) else block:- The code which will be executed if there is no exception is written inside
    the else block.
4) finally block:- The code which will be executed irrespective of whether there is an exception or not is written inside the finally block.
syntax:-
        try:
            # Statements which may cause exception
            # Code which may cause exception
        except ExceptionType as ref:
            # ExceptionType is the type of exception which we want to handle
            # ref is the reference to the exception object
            # Statements to handle the exception
        else:
            # Statements to be executed if there is no exception
        finally:
            # Statements to be executed irrespective of whether there is an exception or not
'''