class add():
    def add(self,a,b):
        return (a+b)
class sub():
    def sub(self,a,b):
        return (a-b)

class cal(add,sub):
    def cal(self,a,b):
        res1=self.add(a,b)
        res2=self.sub(a,b)
        print(f"Addition = {res1}\nSubraction={res2}")

test=cal()
test.cal(5,6)

class emp():
    def emp(self):
        print("i am employee")
print("----------------------------")
class frontend(emp):
    def front_dev(self):
        self.emp()
        print("I am frontend")
class backend(emp):
    def back_end(self):
        self.emp()
        print("i am backend")
class Fullstack(frontend,backend):
    def full_stack(self):
        self.front_dev()
        self.back_end()
        print("I am fullstack develoepr")
        
suresh=frontend()
suresh.front_dev()
print("----------------------------")
manihs=backend()
manihs.back_end()
print("----------------------------")
jatin=Fullstack()
jatin.full_stack()
print("----------------------------")
print(Fullstack.__mro__)

