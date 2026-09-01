'''
1) General Copy
2) Shallow copy
3) Deep copy
'''
import copy
l1=[10,20,30,[40,50]]
l2=l1 #general copy
print(len(l2))
l1[1]=18
print(l2)
l2[3][0]=23
print(l1)

# Shallow copy list
print("#############Shalow copy########")
l3=[10,20,30,[40,50]]
l5=copy.copy(l3) #shallow copy
print(len(l2))
l3[1]=18
l3[3][1]=70
print(l3)
print(l5)
l5[3][0]=23
print(l5)
print(l3)

