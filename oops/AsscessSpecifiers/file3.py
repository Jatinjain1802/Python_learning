class BankAccount:
    def __init__(self,name,acc):
        self.name=name
        self._acc=acc
        self.__balance=500
    def view_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"you Deposit {amount}.Your balnce is {self.view_balance()}")
        else:
            print("enter valid amount")
    def withdraw(self,amount):
        if amount<self.__balance and amount>0:
            self.__balance-=amount
            print(f"you withdraw {amount}.Your remaing balnce is {self.view_balance()}")
        else:
            print("enter valid amount")
            
emp1=BankAccount("jatin",34967389)
print(f"You have this much balance {emp1.view_balance()}")
emp1.deposit(5600)
emp1.withdraw(600)
emp1.withdraw(60000)
emp1.withdraw(-600)

