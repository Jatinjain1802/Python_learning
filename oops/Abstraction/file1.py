# from abc import ABC,abstractmethod
# class Application(ABC):
#     @abstractmethod
#     def login(self):
#         pass
# class WebApplication(Application):
#     def login(self):
#         print("Enter username ")
        
# wa=WebApplication()
# wa.login()
from abc import ABC,abstractmethod
class SuccessfulPerson(ABC):
    @abstractmethod
    def earnmoney(self):
        pass
class Youtuber(SuccessfulPerson):
    def earnmoney(self):
        print("Earn money by ads")
class Panipuri_wala(SuccessfulPerson):
    def earnmoney(self):
        print("Earn by seeling panipuri")
class Vegetable_wala(SuccessfulPerson):
    def earnmoney(self):
        print("Earn by selling vegetbale")
wa=Youtuber()
wa.earnmoney()
pa=Panipuri_wala()
pa.earnmoney()
ve=Vegetable_wala()
ve.earnmoney()