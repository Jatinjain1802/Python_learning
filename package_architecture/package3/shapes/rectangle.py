from calculation.multiply import mul
from calculation.addition import add
a=int(input("Enter the l"))
b=int(input("Enter the b"))
def calculate_rectanglearea(a,b):
    print("area of rectangle",mul(a,b))
calculate_rectanglearea(a,b)
def calculate_rectangleperi(a,b):
    print("perimeter of rectangle",(2*(add(a,b))))
calculate_rectangleperi(a,b)