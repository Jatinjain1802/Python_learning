#  Input a string  and check whether character ‘a’ is present,if yes replace with z and print new string.

a=input("Enter the string")
if 'a' in a:
    print(a.replace('a','z'))