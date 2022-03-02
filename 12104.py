"""
#slicing 사용
A, B = input(), input()
newA = A + A[:-1]
Len = len(B)
count = 0
for i in range(Len):
  if newA[i:i + Len] == B:
    count += 1
print(count)
"""
#KMP 사용
import sys


def makeTable(pattern):
    patternSize = len(pattern)
    table = [0] * patternSize
    j = 0
    for i in range(1, patternSize):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def KMP(parent, pattern):
    table = makeTable(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    count = 0
    j = 0
    for i in range(0, parentSize):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == patternSize - 1:
                count += 1
                j = table[j]
            else:
                j += 1
    return count


A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
print(KMP(A + A[:-1], B))

