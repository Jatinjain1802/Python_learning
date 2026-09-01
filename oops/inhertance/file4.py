class Batsman:
    def bat(self):
        print("he is a batsman")
class Balling:
    def ball(self):
        print("he is a baller")
class AllRounder(Batsman,Balling):
    def feild(self):
        self.bat()
        self.ball()
        print("their fore he is a all rounder")

hardik=AllRounder()
print(AllRounder.__dict__)       
hardik.feild()
