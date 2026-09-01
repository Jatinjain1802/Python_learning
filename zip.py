'''
zip function:- it si built in function that comabain multiple iterables
element by element.It create tuples of corresponsding element
from each iterable


syntax:-
        zip (iterable,itreable2,...)

        -Accepted 2 or more iterable
        -Return a Zip object
        -Each element produced is a tuple

NOTE:- it stops ar shortest itreable and used for paring & mapping

'''
l1=[2,4,6,8]
l2=[20,40,60,80,100]
l3=zip(l1,l2)
print(l3)
print(list(zip(l1,l2)))
new_dic={i[0]:i[1] for i in l3}
print(new_dic)


name=["jatin","oyee","heer","sneha"]
marks=[69,70,88,50]
student={k:("Pass" if v>35 else "fail") for k,v in zip(name,marks)}
print(student)
print(student)
