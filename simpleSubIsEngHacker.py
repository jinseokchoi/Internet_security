
import os, copy, pyperclip, simpleSubCipher, detectEnglish, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ITERATION = 40000

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    # Determine the possible valid ciphertext translations.
    print('Hacking Substitution Cipher Using IsEnglish Function...')
    result = hackSimpleSubIsEnglish(message)
    if result == None:
        print('Not Found')
    else:
        print('Decryption Result: %s' %result)

def hackSimpleSubIsEnglish(message):

    tryNum = 1

    while 1:
        # Python programs can be stopped at any time by pressing Ctrl-C (on Windows) or Ctrl-D (on Mac and Linux)
        # brute-force by looping through every possible key
        decKey = getRandomKey()
        print('[%d th try] DecKey: %s' % (tryNum, decKey))
        decryptedText = simpleSubCipher.decryptMessage(decKey, message)

        if detectEnglish.isEnglish(decryptedText) > 0.20:
            # Check with the user to see if the decrypted key has been found.
            print()
            print('Possible Ciphertext hack:')
            print('Key: ' + str(decKey))
            print('Decrypted message: ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

        tryNum += 1
        if tryNum >= ITERATION:
            return None
    return None



def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()