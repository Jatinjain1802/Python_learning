from calculation.multiply import mul
from calculation.addition import add
side=int(input("Enter the side"))
def calculate_squarearea(side):
    print("area of square",mul(side,side))
calculate_squarearea(side)
def calculate_squareperi(side):
    print("perimeter of sqaure",(2*(add(side,side))))
calculate_squareperi(side)