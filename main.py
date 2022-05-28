import heapq
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
input_lines = []
for _ in range(M):
    u, v, w = map(int, input().split())
    if u > v:
        u, v = v, u
    input_lines.append((u, v, w))
    graph[u].append((w, v))
    graph[v].append((w, u))

visited = [False] * (N + 1)
mst = [[] for _ in range(N + 1)]
sum_weight = 0
q = [(0, 1, 0)]
cnt = 0

while q and cnt < N:
    weight, now, last = heapq.heappop(q)
    if not visited[now]:
        visited[now] = True
        mst[now].append((last, weight))
        mst[last].append((now, weight))
        sum_weight += weight
        cnt += 1
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1], now))


def bfs(start, target):
    q = deque([(start, 0)])
    visited[start] = 1
    while q:
        now, max_weight = q.popleft()
        for next in mst[now]:
            if not visited[next[0]]:
                q.append((next[0], max(max_weight, next[1])))
                visited[next[0]] = visited[now] + 1
                if target == next[0]:
                    return max(max_weight, next[1]), visited[next[0]]


for u, v, w in input_lines:
    visited = [0] * (N + 1)
    loop_max_weight, count = bfs(u, v)
    if count == 2:
        print(sum_weight)
    else:
        print(sum_weight - loop_max_weight + w)
