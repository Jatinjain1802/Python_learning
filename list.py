# It tell you about all the thing in the list
l=[1,2,"abc",True,3j] # hwo to create list
print(l)
print(type(l))
a=len(l) # retun the item in the contanier
print("leng of arry",a)
print("==============================")

l2=list() # way to create an empyt list
print(l2)
print(type(l2))

print("============== How to access lsit element=======")
print (l[0]) # +ve indexing
print (l[-1]) # -ve indexing and aslo find the last 
print (l[len(l)-1]) # finding last element
l[2]="Jatin" # updating the vlaue
print (l)
