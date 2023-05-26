from collections import deque
N, K = map(int, input().split())
deq = deque()
for n in range(1, N + 1):
    deq.append(n)
print("<", end="")
while len(deq) > 1:
    for _ in range(K - 1): deq.rotate(-1)
    print(deq.popleft(), end=", ")
print(deq.popleft(), end=">")