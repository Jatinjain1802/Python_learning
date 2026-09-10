print("Start")
print("5")
print("4")
l=[1,2,3,4,5]
try:
    q=int(input("Enter a number: "))
    p=int(input("Enter a number: "))
    print(q/p)
    print(l[p])
except Exception as e:
    print("Exception details:", e)
# except ZeroDivisionError as e:
#     # print("Error: Division by zero is not allowed.")
#     print("Exception details:", e)
# except ValueError as e:
#     # print("Error: Invalid input. Please enter a valid number.")
#     print("Exception details:", e)
# except Exception as e:
#     # print("Error: An unexpected error occurred.")
#     print("Exception details:", e)
# except IndexError as e:
#     # print("Error: Index out of range.")
#     print("Exception details:", e)

# print("2")
print("1")
print("End")