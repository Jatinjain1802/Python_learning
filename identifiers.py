#identifier are names given to something in python. They can be Vairables,Function,classname,methodnames,Packages name,etc.
#Rules
# 1) identifier should not be with digit
name= "Jatin"
print(name)
# 2) Should nto contain any space and beign in the space
studentname="Heer"
print(studentname)
# 3)only underscore(_) os the only special character allowed in identifier in the bing,at the end,in the middle
_studentname="Heer"
print(_studentname)
student_name="Radhee"
print(student_name)
studentname_="Cutie"
print(studentname_)

# 4) Key words can not be used as identifier .
# Keywords:-
# 1) predefine reserved in the python
# 2) their are 35 keywords
# 3) These three ar know as literal. There are:- True,False, None. and other 32 keywords are in lowercase

import keyword
print(keyword.kwlist)


print(int(1+4))
print(complex())

# type() it is used to return the data type of the object
print(type(name))
