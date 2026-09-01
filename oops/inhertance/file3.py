'''heirarchical'''

class minister():
    def display(self):
        print("i am a minsiter")

class hea(minister):
    def health(self):
        minister.display(minister)
        print("i am a health minister\n I do nothing")

class fic(minister):
    def finace(self):
        minister.display(minister)
        print("i am a finace minister")
        
mohan=hea()
mohan.health()
nirmala=fic()
nirmala.finace()

print(fic.__mro__)
        