from payment_method.credit_card import CreditCard
from payment_method.upi import UPI
# payment1=CreditCard()
# payment2=UPI()
class OnlineStore:
    def __init__(self,payment_method):
        self.payment_method=payment_method
    
    def process(self,amount):
       self.payment_method.authenticate()
       self.payment_method.Pay(amount)
       print("Transction completed")  
       
method=int(input("Enter the valid payment method\n 1) Credit card or 2) UPI \n(Enter 1 or 2)\n")) 
amount=float(input("ENter the amount you want to pay:"))
match method:
    case 1:
        payment1=CreditCard()
        t1=OnlineStore(payment1)
        t1.process(amount)
    case 2:
        payment2=UPI()
        t1=OnlineStore(payment2)
        t1.process(amount)
    case _:
        print("Enter valid case")