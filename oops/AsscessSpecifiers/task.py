class BusinessWoman:
    def __init__(self,name,businesstype,profit):
        self.name=name
        self.businesstype=businesstype
        self.__profit=profit
    
    def __share_dividend(self):
        div=self.__profit*0.1
        print(f"{div} is just a small portion of {self.__profit}")
        print(f"Dividend : {div}")
        self.__profit=self.__profit+div
        print(f"Final Profit: {self.__profit}")
    
    def income_tax(self):
        print(f"Name: {self.name}")
        print(f"Business: {self.businesstype}")
        print(f"Profit: {self.__profit}")
        self.__share_dividend()

w=BusinessWoman("Heer","Cafe_restor",100000)
w.income_tax()
        