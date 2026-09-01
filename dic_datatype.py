# Dictonary
# It is predefined class in python
print("================Dictonary=================")
dic={}
d2={1.1:10,2:30,4:50}
print(dic)
print(type(dic))
print(len(dic))
print("===========how to access Dictonary=============")
print(d2)
print(d2[2]) # this will return error if the key is nto present.
print("========modify and add vlaue in Dictonary========")
print(d2)
d2[1.1]=200
d2[300]=200
print(d2)
print("==============length of Dictonary=============")
print(len(d2))
print("=======key cannot be duplicate============")
d3={1.1:10,1.1:30,4:50,4:60}
d3[1.1]=200000
print(d3)
print("================Methods=================")
# Methoods
print("================get=================")
# 1) get() {ref.get(key)}
# it return the value if the key is present. else it return None
print(d2.get(2))
print("=================setdefault methods================")
# 2) setdefault() {ref.setdefault(key,value)}
# if the key is not present it will add the key with the value. If we dont provide the vlaue then it will take 'None' as the value by default
# if the key is already present it return that value.
d2.setdefault(5,300)
print(d2)
print("=================update methods================")
# 3) update() {ref.update(dic)}
print(d2)
d4={1.11111: 200, 23333: 30, 45555: 50}
d2.update(d4)
print(d2)
print("=================pop methods================")
# 4) pop() {ref.pop(key)}
# it return the value and remove that specific item
rev_value=d2.pop(23333)
print(rev_value)
print(d2)
print("=================popitem methods================")
# 5) popitem() {ref.popitem(object)}
# it remove the last item form the dictionary
item=d2.popitem()
print(item)
print(d2)
print("=================clear methods================")
# 6) clear() {ref.clear()}
# remvoe the all the element of the dic
d3.clear()
print(d3)
print("=================key methods================")
# 7) key() {ref.key()}
# display all the key of the dictionary
key=d2.keys()
print(key)
print("==============values methods================")
# 8) values() {ref.values()}
# display all the value in the dictionary
value=d2.values()
print(value)
print("==============items methods================")
# 9) items() {ref.items()}
# it display /return the item in the tuple
item=d2.items()
print(item)
print("==============fromkeys methods================")
# 10) formkeys(collection of key,optional vlaue) {ref.formkeys(collection,optionalvlaue)}
#it creates a dictionary with each key having optional vlaue. if no optional vlaue is given then 'None' is the optional vlaue
d5={}
nd=d5.fromkeys([1,2,3],300)
print(nd)



