class Person():
    def __init__(self,name,age,gender,nationality):
        self.name=name
        self.age=age
        self.gender=gender
        self.nationality=nationality

class Citizen(Person):
    def __init__(self, name, age, gender, nationality,citize_id):
        super().__init__(name, age, gender, nationality)
        self.citize_id=citize_id
        print(self.__dict__)

class Refugee(Person):
    def __init__(self, name, age, gender, nationality,refugee_id):
        super().__init__(name, age, gender, nationality)
        self.refugee_id=refugee_id
        print(self.__dict__)
        
ravi=Refugee("name",23,"Male","PK","EMAP45")
print(ravi.__dict__)
jatin=Citizen("JAitn",24,"Male","India","EMP3467")


        