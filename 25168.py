from collections import deque

N, M = map(int, input().split())
time = [[0] * (N + 1) for _ in range(N + 1)]
inDegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
result = [0] * (N + 1)
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1
    time[a][b] = t

q = deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        q.append(i)
        result[i] = 1

while q:
    now = q.popleft()
    for next in graph[now]:
        if time[now][next] >= 7:
            result[next] = max(result[next], result[now] + time[now][next] + 1)
        else:
            result[next] = max(result[next], result[now] + time[now][next])
        q.append(next)
print(max(result))