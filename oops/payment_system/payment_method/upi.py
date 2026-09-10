from api.payment_api import Payment_API
from random import randint
class UPI(Payment_API):
    def authenticate(self):
        pin=randint(1000,9999)
        print(f"UPI pin is verified {pin}")
        print("UPI is verified")
    def Pay(self, amount):
        trancitid=randint(100000,99999999999)
        print(f"Transcation id is {trancitid}")
        print(f"Paid {amount} using api")
