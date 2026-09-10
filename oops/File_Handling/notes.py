'''
File Handling Notes:- In python we have diffent types of file:-
1) Text file:- A text file is a file which contains only text data. The data in a text file is stored in the form of characters. The data in a text file can be read and written using the open() function in python.
2) Binary file:- A binary file is a file which contains binary data. The data in a binary file is stored in the form of bytes. The data in a binary file can be read and written using the open() function in python.
3) Data file:- A data file is a file which contains data in a specific format. The data in a data file can be read and written using the open() function in python.
-----------------------------------------------------------------------------
IMPORTANT FUNCTION wrt to File handling in python:-
1) open() function:- The open() function is used to open a file in python. It establishes a connection between the python program and the file. It return the file  object through which we can perform operations. The syntax of open() function is as follows:-
        open("file_name", "mode")
    We have different modes to open a file in python. The different modes are as follows:-
    a) 'r' :- This mode is used to open a file in read mode. if the file does not exist, it will raise FileNotFoundError. Operation in "r:-
        1) 
    b) 'w' :- This mode is used to open a file in write mode.
    c) 'a' :- This mode is used to open a file in append mode.
    

'''