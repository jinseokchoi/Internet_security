__author__ = 'JinSeok Choi'

import pyperclip, sys, random
import simpleSubCipher,detectEnglish

import pyperclip, sys, random, simpleSubCipher, detectEnglish

ITER = 100000
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    #myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    eMessage = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    result = simpleSubIsEnglishHacker(eMessage)

    if result == None:
        print('Not found')

    else:
        print('Decrypted Messag: %s' % result)

def simpleSubIsEnglishHacker(eMessage):
    tryNum = 1
    while tryNum <= ITER:
        #myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
        decKey = simpleSubCipher.getRandomKey()
        #myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

        plainText = simpleSubCipher.decryptMessage(decKey, eMessage)
        print()
        print('Possible encryption hack:')
        print('Key: ' + str(decKey))
        print('Decrypted message: ' + plainText[:100])

        if(detectEnglish.isEnglish(plainText)):
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return plainText

        tryNum += 1

    return None

if __name__ == '__main__':
    main()