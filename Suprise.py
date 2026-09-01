#q3
name=input("Enter any name")
first_name=name[0:3:]
last_name=name[-1:-4:-1]
new=first_name+last_name
'''
li=list(new)
li.reverse()
rev="".join(li)
'''
cs=new[::-1]
print(cs.upper())


#Q5

i="  10 20 30   "
ls=i.strip()
cs=ls.split()
print(int(cs[0])+int(cs[-1]))
