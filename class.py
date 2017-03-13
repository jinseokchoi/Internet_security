__author__ = 'JinSeok Choi'

import operator

def getFrequencyOrder(file):
    resultList =[]
    getWordDict={}
    fpo = open(file, 'r')

    for key in fpo.read().split():
        if key not in getWordDict:
            getWordDict.update({key:1})
        else:
            getWordDict[key] += 1

    fpo .close()

    print (getWordDict)
    # dictionary는 정렬해서 출력해야함 sorted
    for word in sorted(getWordDict.items(), key=operator.itemgetter(1), reverse=True):
        resultList.append(word)

    return resultList

result =  getFrequencyOrder('frankenstein.txt')

for i in range(5):
    print (result[i])