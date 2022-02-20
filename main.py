N = int(input())
word = [input() for _ in range(N)]
temp = word.copy()
newWord = []
for _ in range(26):
    if len(word) == 0:
        break
    maxLength = 0
    maxIndex = 0
    for i in word:
        if len(i) >= maxLength:
            maxLength = len(i)
            maxIndex = word.index(i)
    if word[maxIndex][0] not in newWord:
        newWord.append(word[maxIndex][0])
        if len(word[maxIndex]) > 1:
            word[maxIndex] = word[maxIndex][1:]
        else:
            word.remove(word[maxIndex])
    else:
        if len(word[maxIndex]) > 1:
            word[maxIndex] = word[maxIndex][1:]
        else:
            word.remove(word[maxIndex])
    print(word, newWord)

word = temp
wordSum = 0
for i in word:
    i = list(i)
    i.reverse()
    Sum = 0
    for digit in range(0, len(i)):
        Sum += (10 ** digit) * (9 - newWord.index(i[digit]))
    wordSum += Sum
print(wordSum)

"""
반례
ABBAA
BABBB
188987
2
BABBB
ABBAA
188787
"""
