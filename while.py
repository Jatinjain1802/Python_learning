'''
while loop-
- while is a keyword in pthon
- it is used when we DO NOT know how many times to loop
- it will run until the condition become false
'''
l=[10,20,30,40,50,60,70,80,90,100]
'''
i=1
while i<len(l):
    print(l[i])
    i=i+2  
'''
'''
loop control statement:-
they are ysed to provide extra control or interruption during the loop
excuation
1) break
-it is a keyword in python
-break stops the loop immediately and exit completly, any statamenet which are present
-used to save time by avoiding unnecessary looping execution
2) continue - it is a keyword in pyhotn
-it does not stop , it only skips the current iteration and the below
lines of code inside the loop for that iteration
- it is used to ignore unwanted cases
3)pass- it is key word

'''
l=[23,42,11,56,32,-4,6,-6,7]
d={1:"jatin",2:"jatin"}
for i in range(0,len(l),1):
    if l[i]<0:
        break
   # print(l[i])
sti="jatin"
for i in sti:
    if i=="a":
        #print("s")
        continue
    #print(i)
for i in range(1,11,1):
    if i%4==0:
        continue
    print(i)
marks=[11,20,-3,4,100,-11,23,79]
for i in marks:
    if i<0:
        continue
    print(i)
'''
# nested loop :- a for loop placed inside another loop
- when outer loop runs once, the inner loop completes its entire
iteration
'''
for i in range(7,10):
    for j in range(1,4):
        print(f"{i}*{j}={i*j}")

'''
for-else loop->
in this loop, else block will execute only when the loop normally
completes its iteration without encountering break keyword
-if the loop encounters break keyword,else block will be skipped
'''
roll=[23,1,34,4,7,3]
for i in roll:
    if i==6:
        print("roll no. found")
        break
else:
    print("roll no. not found")














    
