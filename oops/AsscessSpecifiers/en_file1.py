class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0
        self.__fees=0
    @property
    def marks(self):
        return self.__marks
    @property
    def fees(self):
        return self.__fees
    @marks.setter
    def marks(self,newmarks):
        if newmarks>0 and newmarks<101:
            self.__marks=newmarks
            # print(self.__dict__)
        else:
            print("Invalid marks")
    @fees.setter
    def fees(self,newfees):
        if newfees>0:
            self.__fees=newfees
        else:
            print("Enter valid fees")
            
s1=Student("manish")
s1.marks=79
s1.fees=670000
print(s1.marks)
print(s1.fees)
