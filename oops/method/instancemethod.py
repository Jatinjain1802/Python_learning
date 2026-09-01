class employee:
    def __init__(self,name,age,city,dept,salary):
        self.name=name
        self.age=age
        self.city=city
        self.dept=dept
        self.salary=salary
    def display_detial(self):
        return self.__dict__
    def check_salary(self,amount):
        self.salary=self.salary-amount
        return self.__dict__
emp1=employee("jatin",23,"indore","CSE",200000)
emp2=employee("mansih",23,"pune","HR",35000)
emp3=employee("heer",23,"indore","CSE",200000)
emp4=employee("sneha",23,"indore","CSE",20000)
print(emp1.display_detial(),emp2.display_detial(),emp3.display_detial(),emp4.display_detial(),sep="\n")
print("-----------------------------------------")
print(emp1.check_salary(2000),emp2.check_salary(20000),emp3.check_salary(4000),emp4.check_salary(500),sep="\n")

class resturant:
    def __init__(self,name,location,rating):
        self.name=name
        self.location=location
        self.rating=rating
    def display_resturant(self):
        print(self.__dict__)
    def update(self,rating):
        self.rating=rating
        return self.__dict__

res1=resturant("THQ","Ujjain",4.9)
res2=resturant("Onesta","bengulruru",5)
print("-------------------------------------------")
res1.display_resturant()
res2.display_resturant()
print("-----------update----------")
print(res1.update(4.5))
print(res2.update(4.5))


        