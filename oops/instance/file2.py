class Student:
    course="python"  #class varibale inside the class
    class_room=201
    
Student.institute="DCL"   #class varibale outside the class
Student.YOP=2026
print(Student.institute)
obj1=Student()
obj1.course="MERN"   # create instanse variable
print(obj1.__dict__)
print(obj1.course)
obj1.course="GENAI" 
print(obj1.course)
print(obj1.__dict__)
