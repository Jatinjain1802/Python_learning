'''
passing funciton as an argument is known as higher order function

->it take the another function as a input parameter or returns
another function
-> the function that is passed as an argument is called as Callback

'''
def pyhton_exam(location):
    print("Python exam conducted",location)

def java_exam(location):
    print("java exam conducted",location)

def start_exam(subject):
    subject("Ujjain")

start_exam(pyhton_exam)
start_exam(java_exam)
