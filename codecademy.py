__author__ = 'JinSeok Choi'
import pyperclip

number = [5, 6, 7, '8']

print(number)
print(number[3])

number[3] = 10
print(number)

#alpha = ['a', 'b', 'c', 'd', 'e']


message = "ab"
alpha = "ABCDEFGHIJKLMNOPQERSTUVWXYZ"
message = message.upper();
trans = ''
k = 10

for symbol in message:
    temp=alpha.find(symbol)
    trans += (alpha[(temp+k)%len(alpha)])  #25�� ������ �ܾ��� ���� �����Ƿ� �����߻��� ó������

print (trans)

'''
upper_message = message.upper()
print (upper_message)

for i in message:
    print(i)'''