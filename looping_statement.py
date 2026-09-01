'''
looping statement basiclly means a set of intrusction multiple times unitl a
condition is satisfied
-> looping is used to traverse collection element of collection element
->



Why:-
1) it is used to avoid code duplication/ repeation
2) automate repetitive task
3) loops are used to work with collection(list,tuple,string,etc)

types of loop :-
1) for
-> for is used as keyword.
-> it is used when we know in advance how many times we need to loop
-> work very well with range() and collection
-> sytx:-
for {variable} in {sequence}:
    # for block code

in this :
a) variable = it recives one element /item form the sequence at a time
b) sequence = it can be list ,tuple,str,etc
c) for block= for each element recived by the variable for loop body will excute
2) while
3) nested for
'''
l=[10,20,30,40,50,60,70,80,90,100]
for i in range(-1,-len(l),-2):
    print(l[i])
