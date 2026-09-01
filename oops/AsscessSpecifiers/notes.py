'''AccessSpecifiers:-
    -> it apllies only inside Classes,a because Classes are about encapsulation.
    -> Access specifiers are used to set the accessibility of classes, methods, and other members.
    -> These are used to specify the visibility of class members. In python, there are three types of access specifiers:
    1) Public Access Specifier :- 
        -> Any variable or method declared as public can be accessed from anywhere, both inside and outside the class.
        -> no leading underscore is used to declare a public member.
        -> Such var or method can be accessed from any part of the program.Inside the class, outside the class, and even in subclasses.
    2) Protected Access Specifier :- 
        -> Any variable or method declared as protected can be accessed from within the class and its subclasses.
        -> protected is meant for internal usage by child classes.
        -> a single leading underscore is used to declare a protected member.
        -> should be used either in the same class or its child classes. It is not meant to be used outside the class hierarchy.
    3) Private Access Specifier :- 
        -> Any variable or method declared as private can only be accessed from within the class.
        -> a double leading underscore is used to declare a private member.
        -> they cannot be direclty accessed from outside the class. They are meant to be used only within the class itself..
        -> used specially to hide sensitive data.
'''