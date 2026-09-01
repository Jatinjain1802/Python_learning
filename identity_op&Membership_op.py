'''
it is used to comapre the memory locaiton or the memoery address of the object
-> is, is not
-> it return a boolean vlaue
'''
a=5
b=a
print(a is b)

l1=[10,20,30]
l2=l1
print(l1 is l2)

l1=[10,20,30]
l2=[10,20,30]
print(l1 is l2) # two seprate list are made. it focus on memory location
print (l1==l2) # it focus on the vlaue compresion

print("===============Membership op==============")
'''
-> it is used ot check if an element is present in a sequence/collection
-> in , not in
-> it return boolean value
'''
l=[11,22,33,44]
print(11 in l)
print(10 not in l)
print(11 not in l)
print("---tuple---")
t={11,22,33,44}
print(11 in t)
print(10 not in t)
print(11 not in t)
