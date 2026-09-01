a=[2,4,5,2,6,6,8,9,3,6]
a.sort()
a.reverse()
print(a)
high=a[0]

for j in range(1,len(a)):
    if a[j]==high:
        continue
    else:
        print(a[j])
        break
            
            
