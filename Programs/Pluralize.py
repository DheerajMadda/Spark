from collections import Counter
mystr = "cat"


def strOperation(s, codeBlock):
    str = codeBlock(s)
    return str


print(strOperation(mystr, lambda p: p + "s"))

str = "Hello Hello world More Things Test"
strlst = str.split(' ')

uniquewords = set(strlst)

for words in uniquewords:
    print('Frequency of',words,' is',strlst.count(words))