# Sets
print("================Sets=================")
s={10,3,3,2,13,12,30j,40}
print(s)
print(type(s))
print(len(s))
print("================Methods=================")
# Methoods
# 1) set() {ref.add(obj)}
print("================Set methods=================")
s.add(4444)
print("this is s",s)
s.add(998888)
print(s)
print("=================update methods================")
# 2) update () {ref.update(collection)}
# it copies and adds the element from one set to another
s2={10,20,30,40}
s3={5,15,25,35}
s2.update(s3)
print(s2)

print("=================pop methods================")
# 3) pop () {ref.removal()}
# it remove and returns a random element
rem_ele=s2.pop()
print(rem_ele)

print("=================remove methods================")
# 4) remove() {ref.removal(object)}
# it remove a specific object form the set and it should be a member of set
s2.remove(40)
print(s2)

print("=================discard methods================")
# 5) discard() {ref.discard(object)}
# it remove a specific object form the set if object is present. And if objject is not presnet then it does nto show any error
s2.discard(400)
s2.discard(30)
print(s2)


print("=================clear methods================")
# 6) clear() {ref.clear()}
# it remove all the element form the set
s2.clear()
print(s2)

print("=================issubset methods================")
# 7) issubset(set) {ref.issubset(set)}
# it check if one set element are presnet in another set. it return the boolean value {true,false}
s4={10,20,30}
s5={20,30,10,40}
v1=s4.issubset(s5)
print(v1)

print("==============issuperset methods================")
# 8) issuperset(set) {ref.issuperset(set)}
# it check if one set element contain all the element of another set. it return the boolean value {true,false}
s4={10,20,30}
s5={20,30,10,40}
v1=s5.issuperset(s4)
print(v1)

print("==============isdisjoint methods================")
# 9) isdisjoint(set) {ref.isdisjoint(set)}
# it return false if their is any common element in two set. if their is no common elemet in the two set it return true
s4={10,20,30}
s5={20,30,10,40}
v1=s5.isdisjoint(s4)
print(v1)

print("==============union methods================")
# 10) union() {set1.union(set2)}
# it return the new set . which contian the unique element of the both sets
s6={11,22,33}
s7={33,44,55}
v1=s6.union(s7)
print(v1)

print("==============intersection methods================")
# 11) intersection() {set1.intersection(set2)}
# it return the new set . which contian the common element form the both set
s6={11,22,33}
s7={33,44,55}
v1=s6.intersection(s7)
print(v1)

print("==============difference methods================")
# 12) intersection() {set1.difference(set2)}
# it return the new set . which contian element in the 1st set but not in the 2nd set 
s6={11,22,33}
s7={33,44,55}
v1=s6.difference(s7)
print(v1)

print("==============symmetric_difference methods================")
# 13) intersection() {set1.difference(set2)}
# it return the new set . which contian uncommon element of the both sets
s6={11,22,33}
s7={33,44,55}
v1=s6.symmetric_difference(s7)
print(v1)





