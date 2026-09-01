class A:
    def display(self):
        print("Hello this me ")
class B(A):
    def present_project(self):
        print(f"do project {self.__dict__}")
        
es1=B()
es1.display()
es1.present_project()


class developer:
    def code(self):
        print("i am developer")

class frontendclass(developer):
    def design(self):
        print("he design webpage")
        
fd=frontendclass()
fd.code()
fd.design()
print(frontendclass.__mro__)