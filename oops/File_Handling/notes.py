'''
File Handling Notes:- In python we have diffent types of file:-
1) Text file:- A text file is a file which contains only text data. The data in a text file is stored in the form of characters. The data in a text file can be read and written using the open() function in python.
2) Binary file:- A binary file is a file which contains binary data. The data in a binary file is stored in the form of bytes. The data in a binary file can be read and written using the open() function in python.
3) Data file:- A data file is a file which contains data in a specific format. The data in a data file can be read and written using the open() function in python.
syntax:-  f=open("file_name", "mode")
Importnat atrribute in file object
    1) f.name:- teels the file name which is open
    2) f.mode:- gives the mode in which the file is open
    3) f.closed:- used to check whether the file is closed or not and it gives boolen value

File object Methods:-
    1) f.readable():- Checks weather the file is in readebale mode or not . it returns the boolen vlaue
    2) f.writable():- checks weather the file is in writeable mode or not . It return the boolen value
    3) f.close():-  it is used to close the file and release the resources associated with it. In simple terms, it disconnects the program form the file 
-----------------------------------------------------------------------------
IMPORTANT FUNCTION wrt to File handling in python:-
1) open() function:- The open() function is used to open a file in python. It establishes a connection between the python program and the file. It return the file  object through which we can perform operations. The syntax of open() function is as follows:-
        f=open("file_name", "mode")
    We have different modes to open a file in python. The different modes are as follows:-
    a) 'r' :- This mode is used to open a file in read mode. if the file does not exist, it will raise FileNotFoundError. Operation in "r":-
        1) f.read(n):- method of file object,if n is given reads exactly up to n charachter form the current position and return it as string. if n is not given it will read the whole file.
        2) f.readline(n):- reads up to n characters, but only within the current line. is n is not given 
        3) f.readlines():- does not take paramter but it return the list of string, where each string represent the line 
    b) 'w' :- This mode is used to open a file in write mode.If the file exist it will open the file but the previous data of the file is erased. but if the file does not exist a new file will be created and be openned in hte wirte mode . opreration in "w":-
        1) f.write(string):- method of file object used to send the stringdata from python into a file. write() does not automatically add a new line
        2) f.writelines(list):- method of file object which write elements of an iternale to the file. It does not automatically add a newline characters. alwasys their shoukd ve kist of strng, tuple of string
    c) 'a' :- This mode is used to open a file in append mode. it open the file in write mode BUT it retains the existing data, all write operation happen ar the end only,even if seek() is used.if the file does not exist, a new file of that name will be created and be opened in wirte mode
    

'''