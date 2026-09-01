# print(__name__)    #"__main__" only come when the module is direclty excuted
# a=10
# we get the actual module name , when __name__ is executed as result
# importing #package3.
# n=5
# for i in range(0,n):
#     print(i*i)
def add(a,b):
    print(a+b)
if __name__=="__main__":   
     add(10,20) # test code
# how to aviod test code form getting excuted Whenever we imported a member from that module??