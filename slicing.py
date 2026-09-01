'''Extracting a part/portion of a squence datatype
    -> slicing can be done on Indexed based ordered collection
    -> using a special slice operator ":" enclosed within brackets

Syntax:
Sequence[startindex:stopindex:step]

startindex:- it should be int form. from where we begin to slice.
            -> it is inclusive
            -> it also has defuult value . which is 0

stopindex:- index number upto which we slice. it is exclusive
        -> it decided the direction of slicing.
        -> it also has defuult value . which is len(sequence)
        
step:-  it decided how much we wnat to skip the steps
       ->  (+ve -> left to right,-ve-> rigth to left)
       -> defualt value is 1



'''

lis=[10,20,30,40,50,60,70]
tup=[10,20,30,40,50,60,70]
print(lis[-2:-7:-2])
print(lis[::-1])
print(tup[::-1])
cid="0704CS221088"
print(cid[4:6:])
str="Jatin"
print(f"my name is {str}")



test="abracadabra"
char="k"
pos=5
str=test[:int(pos)]+char+test[int(pos+1):]
print(str)


string="ABCDCDC"
sub="c"
res=string.count("CDC")
print(res)
print(res)
