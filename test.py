# Transposition Cipher Test
# http://inventwithpython.com/hacking (BSD Licensed)

# def sequence(n):
#     while n != 1:
#         print (n)
#         if n%2 == 0: # n is even
#             n = n/2
#         else: # n is odd
#             n = n*3+1
#
# sequence(10)
#
# f = 'banana'
# for ch in f:
#     print(ch)

# def add_all(t):
#     total = ''
#     for x in t:
#         total += x
#     return total
#
# t = ['a', 'b', 'c', 'd']
# print (add_all(t))

# t = ['pining', 'for', 'the', 'fjords']
# x = ''.join(t)
# print (x)

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#             print (d)
#         else:
#             d[c] += 1
#             print (d)
#     return d
#
# h = histogram('banana')
# print (h)
#
# spam = 'Four score and seven years is eighty seven years.'
# print(spam[-1])

spam = [1, 2, 3]
eggs = spam
print (eggs)
ham = eggs
print (ham)
ham[0] = 99
print (ham)
print (spam)
print(ham == spam)