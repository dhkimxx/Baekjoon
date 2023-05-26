from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    inDegree[a] += 1

q = deque([])
for i in range(1, N  + 1):
    if inDegree[i] == 0:
        q.append(i)

ans = []
while q:
    now = q.popleft()
    ans.append(now)
    for next in graph[now]:
        inDegree[next] -= 1
        if inDegree[next] == 0:
            q.append(next)
print(len(ans))
