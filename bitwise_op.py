'''
they are used to perform operation on the binary digit(bits) of number

1) bitwise AND op (&)
-> it compare 2 bits and returns 1 when both bits are 1
2) bitwise or op (|)
-> it compare 2 bits and returns 1 if at leates 1 bit is 1
3) bitwi    se XOR op (^)
-> it compare 2 bit and return 1 if both bits are excatly different
4) bitwise NOT op (~)
-> it inverts the bit. 1 became 0 and o became 1
5) bitwise leftshift op (<<)
-> shift the bit to the left side by the no. of positions given
6) bitwise rightshift op (>>)
-. shift the bit to the right side by the no. of position given
'''
a=12
print(12&5)
print(12|5)
print(12^5)
print(~12) #-(a+1)
print(a<<2) # (a*2^no. of position we want to shift)
print(a>>2) #(a/2^no. of position we want to shift)
