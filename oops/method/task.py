class movie_ticket:
    theatre="gopalan"
    gst=18
    @classmethod
    def display(cls):
        print(cls.theatre,cls.gst)
    @classmethod
    def gst_hike(cls,increment):
            cls.gst=cls.gst+increment
            print(cls.theatre,cls.gst)
    #instance 
    def __init__(self,seatno,movie_name,is_adult):
        self.seatno=seatno
        self.movie_name=movie_name
        self.is_adult=is_adult
    def display_obj(self):
        print(self.__dict__)
    @staticmethod
    def calculate_bill(obj,ticketprice,quantity):
        totalprice=(ticketprice*quantity)+(((ticketprice*quantity)*18)/100)
        print(totalprice)
        print(obj.__dict__)

m1=movie_ticket(34,"KGF",True)
m2=movie_ticket(38,"KGF2",False)
movie_ticket.display()
movie_ticket.gst_hike(2.5)

m1.display_obj()
m2.display_obj()
m1.calculate_bill(movie_ticket,200,3)
# m2.calculate_bill(230,2)

