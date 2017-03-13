__author__ = 'JinSeok Choi'

import  pyperclip, cryptomath

Letter ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

message = 'HELLO'
mulKey=7
addKey=2
trans=''
decrt=''
for i in message:
    if(i in Letter):
        num = Letter.find(i)
        trans+=Letter[(num*mulKey+addKey) %len(Letter)]


print(trans)

invKey=15
cryptomath.findModInverse(mulKey,len(Letter))

for i in trans:
    if(i in Letter):
        num = Letter.find(i)
decrt+=Letter[((num-addKey)*invKey) %len(Letter)]

print(decrt)

list=[]
for i in range(2,len(SYMBOLS)):
    if cryptomath.gcd(len(SYMBOLS), i) == 1:
        list.append(i)

print(list)
print(len(list))