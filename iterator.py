'''
Iterator:- It is pyhton is an object that allows you to reaverse
 through all elemet of a collection. One at a time. without needing
 to know about the colllection (weather unstrucutre or structure)

 ->it is unidirectional(goes form left to right only)
 -> support partial iteration (stop where we want)

eHAS PREDEFINE TWO FUCNTION:-
1)iter(iterable)
    -> iter() takes an iterable (list,string,tuple....)
    and return iterator object. The iterable object keeps a
    cursor (internal pointer) that moves to the next element
    every time next() is called.
2) next(iterable object)
    ->return the next element form the iterator and advance the
    cursor.when no element are left , it raise StopIteration

NOTE:-
    1) it is EXHAUSTABLE (single use object)
    2) for loop internally uses iterator logic
'''
print("+++++++++ways for making iteratore+++++++++++")
print("+++++++++1st way+++++++++++")
l=[1,2,3,4,5]
#print(type(l))
obj=iter(l)  #creation of iterable object
print(obj)  #shows the memory address
e1=next(obj)   # return the element from the collection
print(e1)
e2=next(obj)
print(e2)
e3=next(obj)
print(e3)
e4=next(obj)
print(e4)
e5=next(obj)
print(e5)
print("+++++++++2nd way+++++++++++")
l2=[10,20,30,40,50,60,70,80,90,100,120,121,122,123,124,125,125,125,1424]
itr_obj=iter(l2)
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))
print("--------------------------")
 # accesscing each element using the for loop without next
for i in itr_obj:  #second way of calling 
    print(i)

print("+++++++++3rd way+++++++++++")
l3=[4,3,2,5,6,7,8,9,8,7,86,67,67,688,56,43,22]
itrr_obj=iter(l3)
print(list(itrr_obj))
