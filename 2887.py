import heapq
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
P = [list(map(int, input().split())) + [i] for i in range(N)]
for i in range(3):
    P.sort(key=lambda x: x[i])
    for j in range(1, N):
        graph[P[j-1][3]].append((abs(P[j - 1][i] - P[j][i]), P[j][3]))
        graph[P[j][3]].append((abs(P[j - 1][i] - P[j][i]), P[j-1][3]))

q = [(0, 0)]
visited = [0] * N
ans = 0
while q:
  cost, now = heapq.heappop(q)
  if not visited[now]:
    visited[now] = 1
    ans += cost
    for next in graph[now]:
      heapq.heappush(q, (next[0], next[1]))
print(ans)