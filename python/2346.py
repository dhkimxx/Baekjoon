from collections import deque

_ = input()
deq = deque(enumerate( list(map(int, input().split()))))
results = []

while deq:
    index, value = deq.popleft()
    results.append(index + 1)

    if value > 0:
        deq.rotate(-(value - 1))
    else:
        deq.rotate(-value)

print(' '.join(map(str, results)))