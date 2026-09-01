'''
it is a short hand way of writing if else in one line of code


if num>0:
    print("Positive")
else:
    print("Negative")
'''
# TrueExp if condition else falseExp
num=12
#print("postive") if num>0 else print("Negative")
result="positve" if num>0 else "Negative"
print(result)
age=int(input("enter the age"))
eligible="eligible" if age>=18 else "not eligible"
print(eligible)
nums=-7
res=nums+10 if nums>0 else nums-5
print(res)
