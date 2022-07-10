from collections import deque

N, M = int(input()), int(input())
P = list(map(int, input().split()))
visited = [0] * (N + 1)
distance = [1e9] * (N + 1)

q = deque(P)
bin = []
visited[P[0]] = 1
while q:
    v = q.popleft()
    for i in bin:
        temp = sum(list(map(int, bin(v ^ i))))
        if distance[v] > temp:
            distance[v] = temp
    bin.append(v)



