'''
range is a class and it was implemented in python3
-> whenever we call range(), we are actually creating a range object
-> range is an immutable sequence type(like tuple,string)

syntx:
range(stop)
range(start,stop)
range(start,stop,step)

here:
start:- The number to begin with. It is inclusive. Defalut vlaue is 0
stop:- the number upto which it is going. it is exclusive. No defualt vlaue
step:- it decides by how much to move for each number. in this if we use positive number it is used ofr increment and negative number for decrement. defualt vlaue is 1

feature :-
1) Immutable
2) Lazy/ Memory efficient- range doesnot generate all number at once
3) Iterable:- it can be used with for loop
4) It support indexing and slicing

importance
1) used to when we need a sequence of number(couting.indexing)
2) it is used in for loop to iterate specific number of itme
3) to avoid creating large list in the memory

'''
a=range(13,0,-3)
print(list(a))
print(list(range(-13,0,3)))

