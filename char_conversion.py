'''
changing char into its numeric value (unicode) and vise versa

-> part of typecasting
-> python internally represnet every charcter by a unicode code point

2 function involved in character conversion
1) ord("character"):- pre define funtion that returns the unicode of the
of the given character. it return the int value.
A->65 to Z-> 90
a->97 to z-> 122
 ->32
0->48 to 9->57


2)chr(int)
here int is unicode value 
pre define function
return the corresponding charater which is assoctiated for the number

'''


unicode=ord("A")
char=chr(179503)
print(char)
