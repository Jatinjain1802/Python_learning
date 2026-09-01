class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        print(f"{name} {roll}")
        print(self.__dict__)
class SchoolStudent(Student):
    def __init__(self, name, roll,principle):
        super().__init__(name, roll)
        self.principle=principle
        print(f"{name} {roll} {principle}")
        print(self.__dict__)
        
        

s=SchoolStudent("sharma",34,"deshpandey")
# print(s.__dict__)
        