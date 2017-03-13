# Detect English module
# http://inventwithpython.com/hacking (BSD Licensed)

# To use, type this code:
#   import detectEnglish
#   detectEnglish.isEnglish(someString) # returns True or False
# (There must be a "dictionary.txt" file in this directory with all English
# words in it, one word per line. You can download this from
# http://invpy.com/dictionary.txt)
import codecs
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\r\n'

dictionaryFile = codecs.open('diet_complete_korean_letters_2350.txt','r','utf-8')

for word in dictionaryFile.read().split('\r\n'):
    LETTERS_AND_SPACE = LETTERS_AND_SPACE + word
dictionaryFile.close()

def loadDictionary():
    englishWords = {}
    dictionaryFile = codecs.open('diet_english_korean_dictionary.txt','r','utf-8')

    for word in dictionaryFile.read().split('\r\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0 # no words at all, so return 0.0

    matches = 0

    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1

    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglishOrKorean(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))

    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage

    return wordsMatch and lettersMatch