'''
s12="jatin+is+happy"
email="jjain0740@gmail.com"
rep=email.replace("@gmail.com","")
lis=rep.split()
print(rep)
print(lis[0])
print(email.split("@gmail.com"))
print(len(lis))
'''

l2={"16","07","2026"}
print("".join(l2))


name="jatin"
namee=tuple(name)
print(namee)

def change(name):
    result = ""
    print(len(name))
    for i in range(len(name)):
        if i % 2 == 0:
            result += name[i].lower()
            print(result)
        else:
            result += name[i].upper()

    return result


name = "independance day"
print(change(name))
