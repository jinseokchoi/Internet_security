__author__ = 'JinSeok Choi'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'


def checkValidKey(key):
    if list(LETTERS).sort() != list(myKey).sort():
        return 'false'

message = "Hello"

mode = 'encrypt'

translated=''

checkValidKey(myKey)

if mode == 'decrypt':
    LETTERS, myKey = myKey, LETTERS

for i in message:
    if i.isupper():
        translated += myKey[LETTERS.find(i)]
    else:
        translated += myKey[LETTERS.find(i.upper())].lower()

print(translated)