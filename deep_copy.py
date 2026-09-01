import copy
l1=[10,20,30,[40,50]]
l2=copy.deepcopy(l1) #deep copy
print(len(l2))
l1[1]=18
print(l2)
print(l1)
l2[3][0]=23
print(l2)
print(l1)
