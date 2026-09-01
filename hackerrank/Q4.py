n = int(input("Number of elements: "))
lst = []
marks=[]
for i in range(n):
    a = input("Enter the name: ")
    b = float(input("Enter marks: "))
    lst.append([a, b])

for j in lst:
    marks.append(j[1])
marks.sort()
low=marks[0]
count=marks.index(marks[0])
for i in range(1,len(marks)):
    if marks[i]==low:
        continue
    else:
        #print(marks[i])
        sec_lrg=marks[i]
        #print(count)
name=[]
for i in lst:
    if i[1]==sec_lrg:
        name.append(i[0])
name.sort()
for i in name:
    print(i)
