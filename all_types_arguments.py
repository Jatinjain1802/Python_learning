def order_food(hotel_name,*menu,drink="water",**maincourse):
    print(hotel_name)
    print(*menu)
    print(drink)
    print(maincourse)
menu=["panner65","frecnhfries","panner tikka"]

    
order_food("namaste",*menu,roti="butter naam",gravy="kajumasla")
