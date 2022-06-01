from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
time = [0] * (N + 1)
result = [0] * (N + 1)
for a in range(1, N + 1):
    time[a], *temp = map(int, input().split())
    for b in temp[:-1]:
        inDegree[a] += 1
        graph[b].append(a)

q = deque([])
for i in range(1, N + 1):
    if inDegree[i] == 0:
        result[i] = time[i]
        q.append(i)

while q:
    now = q.popleft()
    for next in graph[now]:
        inDegree[next] -= 1
        result[next] = max(result[next], result[now] + time[next])
        if inDegree[next] == 0:
            q.append(next)
print('\n'.join(map(str, result[1:])))
