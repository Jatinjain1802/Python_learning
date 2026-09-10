from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         a=self.l*self.b
#         print(a)

# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         a=self.side**2
#         print(a)

# s1=Square(23)
# s1.area()
# s2=Rectangle(3,4)
# s2.area()


class Trainer(ABC):
    @abstractmethod
    def train(self):
        pass
    @abstractmethod
    def conduct_mock(self):
        pass

class Python(Trainer):
    def __init__(self,name):
        self.name=name
    def train(self):
        print(f"{self.name} i a trainer")
    def conduct_mock(self):
        print(f"{self.name} takes mock")
    def check(self):
        self.train()
        self.conduct_mock()

class SQL(Trainer):
    def __init__(self,name):
        self.name=name
    
    def train(self):
        print(f"{self.name} i a trainer")
    def conduct_mock(self):
        print(f"{self.name} takes mock")

class Front_end(Trainer):
    def __init__(self,name):
        self.name=name
    def train(self):
        print(f"{self.name} i a trainer")
    def conduct_mock(self):
        print(f"{self.name} takes mock")

p1=Python("chetan")
p1.check()
q1=SQL("jatin")

        