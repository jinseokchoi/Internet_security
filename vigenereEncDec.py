__author__ = 'JinSeok Choi'

def main():
    message ="Common sense is not so common"
    key = "Pizza"
    key=key.upper()
    mode ="encrypt"
    EncryM =Vignere_Encrypt1(message,key)
    print(EncryM)
    Vignere_Decrpyt1(EncryM,key)




def Vignere_Encrypt1(message,key):
    LETTERS ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    trans=[]
    Key_Index=0
    message =message.upper()
    for i in message:
        if LETTERS.find(i) != -1:
            trans.append(LETTERS[(LETTERS.find(i)+LETTERS.find(key[Key_Index])) % len(LETTERS)])
            Key_Index +=1
        else:
            trans.append(i)
            Key_Index +=1
        if(Key_Index == len(key)):
            Key_Index=0

    return ( ''.join(trans))

def Vignere_Decrpyt1(message,key):
    decMessage=[]
    Key_Index =0
    LETTERS ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in message:
        if LETTERS.find(i) != -1:
            decMessage.append(LETTERS[(LETTERS.find(i)-LETTERS.find(key[Key_Index])) % len(LETTERS)])
            Key_Index +=1
        else:
            decMessage.append(i)
            Key_Index +=1
        if(Key_Index == len(key)):
            Key_Index=0
    print(''.join(decMessage))


if __name__ == '__main__':
    main()