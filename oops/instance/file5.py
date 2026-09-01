class Student:
    def __init__(self,name,filmname,industruy):   #constructore
        # print("constructore")
        self.name=name
        self.filmname=filmname
        self.industruy=industruy
        self.gender="Female"
        
        print(self.__dict__)

s1=Student("kareena","xyz","bollywood")
# print(s1.__dict__,"bhar vala")
s2=Student("katrina","zyx","bollywood")
# print(s2.__dict__,"bhar vala")
s3=Student("srivali","animal","tollywood")

