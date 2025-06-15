pan = set('The quick brown fox jumps over the lazy dog'.lower())
alphabet = set('abcdefghijklmnopqrstuvwxyz ')

def check(str):
    if (len(alphabet-str)) == 0:
        print('Is a panagram')
    else:
        print('Is not a panagram')
check(pan)
print(len(alphabet-pan))

sentA = set('The sky is blue'.lower().split())
sentB = set('Water is not blue'.lower().split())
print(sentA & sentB)

a = set('The frog is green'.lower())
b = set('The elephant is grey'.lower())
vowels = set('aeiou')
consonants = alphabet-vowels
print(a-consonants)

c = (1,2,3,4)
d = list(c)
d[3] = 1
c = tuple(d)
print(d,c)