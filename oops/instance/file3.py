class Employee:
    company="DCL"
    location="ben"

# print(Employee.__dict__)
print(Employee.company)
print(Employee.location)

emp1=Employee()
emp1.fname="jatin jain"
emp1.id="EMP1"
# print(emp1.__dict__)
print(emp1.fname)
print(emp1.id)

emp2=Employee()
emp2.fname="manish"
emp2.id="EMP2"
# print(emp2.__dict__)
print(emp2.fname)
print(emp2.id)
