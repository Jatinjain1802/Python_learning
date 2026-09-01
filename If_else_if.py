'''
if-else-if is used when there are multiple condition to check and
ONLY 1st MATCHING coddition and its block will be ecuted

NOTE:-
-> When we want many choice but ONLY one should aplly
->elif is keyword in python and can be repeated any number of times

'''
marks=float(input("Enter your marks"))
if marks>=90 and marks<=100 :
    print("You are topper")
elif marks>=80 and marks<=100:
    print("Distintion")
elif marks>=60 and marks<=100:
    print("1st Class")
elif marks>=40 and marks<=100:
    print("2nd Class")
elif marks>=35 and marks<=100:
    print("pass")
elif marks>=0 and marks<=100:  :
    print("Future of india")
