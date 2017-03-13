__author__ = 'JinSeok Choi'

import simpleimport, math

key = 8
ct = ['a'] * key
print (ct)

print ("".join(ct))

str_a = "abcd"
str_b = "efgh"

print (str_a.join(str_b))

for i in range(10):
    print (i)

list_a = [1, 2, 3]
list_b = [4, 5, 6]

print (list_a + list_b)

list_a = list(str_a)
print (list_a)

result = ['Ceno', 'onom', 'mstm', 'me o', 'o sn', 'nio.', ' s ', 's c']
print ("".join(result))

dictionaryFile = open('dictionary.txt')
englishWords = {}
for word in dictionaryFile.read().split('\n'):
    englishWords[word] = None

dictionaryFile.close()
print (len(englishWords)) #사전에 있는 단어의 갯수 확인