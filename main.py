import sys

N = int(sys.stdin.readline())
card = []
for n in range(1, N + 1):
    card.append(n)
while len(card) > 1:
    card.pop(0)
    card.append(card.pop(0))
print(card)