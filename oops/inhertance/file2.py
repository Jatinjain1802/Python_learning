'''Multilevel inhertance'''
class Vehical:
    def move(self):
        print("it moves")

class Bike(Vehical):
    def ride(self):
        print("it speed with ride")

class ElectricBike(Bike):
    def charge(self):
        print("it charge")
        
ather=ElectricBike()
ather.move()
ather.ride()
ather.charge()
print(ElectricBike.__mro__)