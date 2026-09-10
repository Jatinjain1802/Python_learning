from api.payment_api import Payment_API
from random import randint

class CreditCard(Payment_API):
    def authenticate(self):
        otp=randint(100,999)
        print(f"Credit card OTP verfied{otp}")
        print("Credit card authentication successfull")
    def Pay(self,amount):
        transctid=randint(100000,9999999999999)
        print(f"Transction id {transctid}")
        print(f"{amount} is paid")

# amount=float(input("Enter the amount you want to pay"))