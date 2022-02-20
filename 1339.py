N = int(input())
word = []
for _ in range(N):
    word.append(list(input()))

rank = {}
for W in word:
    for w in W:
        rank[w] = 0

for n in range(len(word)):
    word[n].reverse()
    for m in range(len((word[n]))):
        rank[word[n][m]] += 10 ** m
sortedRank = sorted(rank.items(), key=lambda x : x[1], reverse=True)

Sum = 0
for dic in sortedRank:
    Sum += (9 - sortedRank.index(dic)) * dic[1]
print(Sum)