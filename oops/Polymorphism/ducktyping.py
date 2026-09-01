class Zomato:
    def deliver(self):
        print("Zomato is delivering food")

class Swiggy:
    def deliver(self):
        print("Swiggy is delivering food")

class UberEats:
    def deliver(self):
        print("UberEats is delivering food")
        
class Poter:
    def transport(self):
        print("Poter is delivering Good and material")
        
def process (partner):
    partner.deliver()


z=Zomato()
s=Swiggy()
u=UberEats()
p=Poter()

l=[z,s,u,p]
for i in l:
    # try:
    #     process(i)   
    # except AttributeError:
    #     print(f"{i.__class__.__name__} does not have deliver method") 
    if hasattr(i, 'deliver'):
        process(i)
    else:
        print(f"{i.__class__.__name__} does not have deliver method")