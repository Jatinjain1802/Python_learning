'''
it is used in API. datafram in pandas.
'''
company={
        "name":["Amy","Ben","Chad"],
        "ages":[21,32,48],
        "salary":[82000,48000,36000],
        "depts":["HR","sales","Account"]
    }
print(company)
for i in company:
    print(company[i][0])
    print(company[i])
