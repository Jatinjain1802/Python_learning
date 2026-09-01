from typing_extensions import override
class Athelet:
    def pushups(self):
        print("10 psuhus")
class Wrestler(Athelet):
    @override
    def pushups(self):
        print("20 pushups")
    
w=Wrestler()
w.pushups()
# w=Athelet()
# w.pushups()

class Minister():
    def address_public(self):
        print("adress public")
class FinacnceMinsiter(Minister):
    @override
    def address_public(self):
        super().address_public()
        print("I address people on fincae thing")

nirmala=FinacnceMinsiter()
nirmala.address_public()

# anil=Minister()
# anil.address_public()       


class Singer():
    def sing(self):
        print("They sing a song")

class ClassicalSinger(Singer):
    @override
    def singer(self):
        super().sing()
        print("they sing classiscal singler song")


asha=ClassicalSinger()
asha.singer()