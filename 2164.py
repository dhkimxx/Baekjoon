from collections import deque
import sys
N = int(sys.stdin.readline())
card = deque()
for n in range(1, N + 1):
    card.append(n)
while len(card) > 1:
    card.popleft()
    card.rotate(-1)
print(card.popleft())