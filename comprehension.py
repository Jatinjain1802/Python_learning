'''
comprehension:- Python way of writitng loops that produce
collections in a compact, readable form.
it combines=> iteration+transformation+filtering

3 types of comprehension
    1) List com:- easier way to creat list . can perform
        (tranformarion+filtering)
        sytanx:-
        1) new_list=[expression 'for' item 'in' sequence]
        2) new_list=[True_expression 'for' item 'in' sequence 'if' condition]
        3) new_list-[True_expression 'if' condition 'else' false_expression 'for' item 'in' sequence]
    2) Set com
        sytanx:-
         sytanx:-
        1) new_set={expression 'for' item 'in' sequence}
        2) new_set={True_expression 'for' item 'in' sequence 'if' condition}
        3) new_set={True_expression 'if' condition 'else' false_expression 'for' item 'in' sequence}
    3) dict com
        sytanx:-
        1)new_dict={key_expression:vlaue_expression 'for' item 'in' iterable}
        2)new_dict={key_expression:value_expression 'for' item 'in' iterable 'if' conditon}
        3)new_dict={key_expression:(True_expression if condition else false_expression) for item in iterable}
        
'''
print("--------list comp--------")
li=[13,23,33,43]
nl=[i+5 for i in li] #sytax1
print(nl)
l=[i**2 for i in li] 
print(l)
fl=[i>30 for i in li]
a=["Tatrun","paratrha","Zen","Yash"]
u_name=[i.upper() for i in a]
uname=[i.upper() for i in a if len(i)>4]
print(u_name)
print(uname)
l2=[11,21,24,34,43]
fl=[i**2 for i in l2 if i%2==0] # sytax 2
print(fl)
l4=[2,3,4,5,6,7]
f2=[i**2 if i%2==0 else i**3 for i in l4] # sytax 3
print(f2)

print("--------set comp--------")
s={2,3}
print(type(s))
print("--------dict comp--------")
l=[2,3,4,5]
dic={i : i**2 for i in l} #sytax 1
print(dic)
l2=["tom","jerry","kid","kat"]
l2_dic={i:len(i) for i in l2}
print(l2_dic)
dic_even={i : i**2 for i in l if i%2==0} #syntax 2
print(dic_even)
dic_l2={i : i.upper() for i in l2 if len(i)>4} #syntax 2
print(dic_l2)
dic_3={i : (i**2 if i%2==0 else i**3) for i in l} #sytax 3
print(dic_3)
d={54:45,20:80,50:5,9:99}
print(d.items())
d_evl={k:("Pass" if v>35 else "Fail") for k,v in d.items()}
print(d_evl)
