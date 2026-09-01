'''
it is a pre define function which is used to display or to show the output on the console/screen
using print we can display multiple vlaues with the help comma
syntax:
print(v1,v2,v3,v4....)

2default argument in print function
1)sep
->whenver multiple values are to be printed in that case the seperatore vlaue
will be printed after each value
-> the default of sep is space, sep=" "
-> if their are n vlaues to be printed the sepratore vlaue will be printed
n-1 times

2) end
-> it will be displayed at the end after printing all the values
-> defualt value of end in \n, end="\n"
-> it will be printed only once at the last
'''
print("--------")
a=input("enter your name")
print(11,22,33,44,55,sep="\n",end=a) # space is used as the sepratore between the vlaues

