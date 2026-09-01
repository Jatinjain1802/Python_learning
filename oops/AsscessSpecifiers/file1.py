class Employee:
    def __init__(self, name, eid,dept,salary):     # Public access specifier
        self.name = name
        self.eid = eid
        self.dept = dept
        self._salary = salary  # Protected attribute
    
    def display(self):          # Public access specifier
        print("Employee Name:", self.name)
        print("Employee ID:", self.eid)
        print("Employee Department:", self.dept)
        print("Employee Salary:", self._salary)   # Protected attribute accessed within the class
    
    def _display_salary(self):  # Protected method
        print("Employee Salary:", self._salary)

class Eng(Employee):
    def display_salary(self):
        self._display_salary()  # Accessing protected method from parent class
emp1=Eng("John Doe", 12345, "HR", 50000)
emp1.display_salary()