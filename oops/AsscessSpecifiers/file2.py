class Politician:
    def __init__(self,name,party,funds):
        self.name=name
        self.party=party
        self.__funds=funds  # Private attribute
    
    def __multiply_funds(self):
        print("Politicians enter into real estate business to multiply their funds.")  # Private method
    
    def file_RTI(self):
        print("Politician Name:", self.name)
        print("Politician Party:", self.party)
        print("Politician Funds:", self.__funds)  # Accessing private attribute within the class
        self.__multiply_funds()  # Accessing private method within the class

p=Politician("Rahul","INC",1000000)
p.file_RTI()  # Accessing public method to display politician details and multiply funds