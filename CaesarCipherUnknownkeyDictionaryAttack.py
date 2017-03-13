# Caesar Cipher Dictionary Attack
# 200958117 김태회 인터넷보안
# 키를 모르는 상태에서 사전 공격을 감행하여 해독된 메세지를 자동으로 찾아본다.
# 시험기능(Experimental) : 한글 메세지 지원

import sys
import codecs
import random
import detectEnglishKorean

class uniCaesarCipher:
    LETTERS = None
    encryptKey = None

    def __init__(self):
        self.LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    def addKoreanLetters(self):
        dictionaryFile = codecs.open('diet_complete_korean_letters_2350.txt','r','utf-8')
        for word in dictionaryFile.read().split('\r\n'):
            self.LETTERS = self.LETTERS + word
        dictionaryFile.close()

    def proceedYourMessage(self, workMode, key, myMessage):
        resultText = ''
        for symbol in myMessage:
            if symbol in self.LETTERS:
                # get the encrypted (or decrypted) number for this symbol
                num = self.LETTERS.find(symbol) # get the number of the symbol

                if workMode == 'encrypt':
                    num = num + key
                elif workMode == 'decrypt':
                    num = num - key

                # handle the wrap-around if num is larger than the length of
                # LETTERS or less than 0
                if num >= len(self.LETTERS):
                    num = num - len(self.LETTERS)
                elif num < 0:
                    num = num + len(self.LETTERS)

                # add encrypted/decrypted number's symbol at the end of translated
                resultText = resultText + self.LETTERS[num]

            else:
                # just add the symbol without encrypting/decrypting
                resultText = resultText + symbol
        return resultText

    def attackWithDictionary(self, message, wordPercentage=20, letterPercentage=85):
        # 가능한 키를 모두 대입하여 Brute-Force 공격을 진행합니다.
        for key in range(len(self.LETTERS)):

            # The rest of the program is the same as the original Caesar program:
            translated = self.proceedYourMessage('decrypt', key, message)

            # 특정 키로 공격된 메세지입니다.
            print('Key #%s: %s' % (key, translated))

            # 각 메세지를 단어들과 대조하여 인간이 읽을 수 있는 메세지인지 검사를 한다.
            if detectEnglishKorean.isEnglishOrKorean(translated,wordPercentage,letterPercentage):
                print()
                print('이 메세지가 맞는 것 같습니까? :')
                print('Key %s: %s' % (key, translated[:100]))
                print()
                print('N을(를) 누르면 중단하고, 다른 키를 누르면 다른 메세지에 공격을 계속 진행합니다 :')
                response = input('$ ')
                if response.strip().upper().startswith('N'):
                    return translated


# 프로그램을 준비한다.
work = uniCaesarCipher()
work.addKoreanLetters()
print('\n특수문자 + 숫자 + 알파벳 + 완성형 한글2350자(KS C 5601) : ', len(work.LETTERS))

# 암호화할 때 사용할 키를 정한다. 그리고 암호화할 메세지를 물어본다.
work.encryptKey = random.randint(1, len(work.LETTERS) - 1)
myMessage = input('암호화할 메세지를 입력해보세요. $ ')
CipherText = work.proceedYourMessage('encrypt', work.encryptKey, myMessage)
print('당신이 입력한 메세지의 암호문입니다. : ', CipherText)

# 공격도 할 것인지 물어본다.
askContinue = input('공격도 해보시겠습니까? 사전을 이용한 공격을 합니다. $ ')
decryptedText = ''
if askContinue.strip().upper().startswith('Y'):
    # 암호문에 사전을 이용한 무작위 공격을 진행 해본다.
    decryptedText = work.attackWithDictionary(CipherText)
    # 한글 메세지 같은 경우에는 영문보다 더 복잡해서, 더 약한 조건으로 다시 검색해볼 수 있는 옵션을 제공
    if decryptedText is None:
        response =input('\nwordPercentage 20 -> 10, letterPercentage 85 -> 40\n단어/문자 검사 강도를 높혀서 다시 검색합니다. (Y/N) $ ')
        if response.strip().upper().startswith('Y'):
            decryptedText = work.attackWithDictionary(CipherText,10,40)
    print('해독된 메세지 : ', decryptedText)
else:
    sys.exit()