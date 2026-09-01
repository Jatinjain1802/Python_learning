'''
nested collection:- it means collection having another collection
inside it

types
1) nested list
2) nested dictionary:- dictonary have another dictonary in it is knwo as nested dictonary
3) list of dictionary
4) dictionary of list
'''
l=[["Amy",80000,"BE"],["Ben",45000,"SSLC"],["Chad",89000,"Diploma"]]
#print(l)
l[1].append("M tech")
#print(l)

company={"emp1":
         {"name":"amy",
          "age":21,
          "salary":80000,
          "dept":"Account"},
         "emp2":
         {"name":"ben",
          "age":32,
          "salary":32000,
          "dept":"sales"},
         "emp3":
         {"name":"chad",
          "age":44,
          "salary":49000,
          "dept":"marketing"}}
tup=company.get("emp1")
'''
for i in company.keys():
    #print(company[i])

for i in company:
    tup=company.get(i)
    for j in tup:
        if tup.get("salary")>50000:
           # print(tup)
            break
        #print(tup)
        
    #print(i)
'''
print("***************************************")
for k,v in company.items():
    #print(v["salary"])
    if v.get("age")>40:
        print(v["name"])
        v["salary"]=v["salary"]+5000
        #print(v["salary"])
        print(v)

print("****************JSON(javascript object notation)***********************")
'''
used to formate and store the stricture data between client and server
in webapp and in API
-> list of dictinary in used in JSON/API
'''

