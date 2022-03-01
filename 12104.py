#https://blog.naver.com/b1327e/222639590710
#12104번 순환 순열
import sys
from collections import deque
A = deque(sys.stdin.readline().rstrip())
B = deque(sys.stdin.readline().rstrip())
count = 0
for n in range(len(B)):
    if A == B:
        count += 1
    B.rotate(-1)
print(count)
