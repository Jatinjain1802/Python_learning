import pickle
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f"{self.name}=>{self.salary}"

emp1=Employee("jatin",45000)
emp2=Employee("mansih",60000)
with open("File_Handling/emp.pkl","w+b") as f:
    # byte=pickle.dumps(emp1)
    # byte1=pickle.dumps(emp2)
    # f.write(byte)
    # f.write(byte1)
    pickle.dump(emp1,f)
    f.seek(0)
    # dd=f.read()
    # print(dd)
    obj=pickle.load(f)
    # obj1=pickle.loads(dd)
    print(obj)
    # print(obj1)
    