import sys
from collections import deque

N = int(sys.stdin.readline())
inDegree = {}
graph = {}
for _ in range(N):
    a, b = sys.stdin.readline().split()
    if inDegree.get(a, -1) == -1:
        inDegree[a] = 0
        graph[a] = []
    if inDegree.get(b, -1) == -1:
        inDegree[b] = 1
        graph[b] = []
    else:
        inDegree[b] += 1
    graph[a].append(b)

q = deque([])
for i in inDegree:
    if inDegree[i] == 0:
        q.append(i)

ans = []
temp = []
q = deque(sorted(q))
while q:
    now = q.popleft()
    ans.append(now)
    for next in graph[now]:
        inDegree[next] -= 1
        if inDegree[next] == 0:
            temp.append(next)
    if not q:
        temp.sort()
        q.extend(temp)
        temp = []

if len(ans) != len(inDegree):
    print(-1)
else:
    print('\n'.join(map(str, ans)))