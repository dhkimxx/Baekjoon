from collections import deque
import heapq
import sys
input = sys.stdin.readline
LOG = 22    # 2^21 = 2,000,000

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
input_lines = []
for _ in range(M):
    u, v, w = map(int, input().split())
    input_lines.append((u, v, w))
    graph[u].append((w, v))
    graph[v].append((w, u))


depth = [0] * (N + 1)
parent = [[0] * LOG for _ in range(N + 1)]
sum_weight = 0
max_weight = 0
LOG_weight = [[0] * LOG for _ in range(N + 1)]
q = [(0, 1, 0)]
cnt = 0

while q and cnt < N:
    weight, now, last = heapq.heappop(q)
    sum_weight += weight
    if not depth[now]:
        depth[now] = depth[last] + 1
        cnt += 1
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1], now))
            parent[next[1]][0] = now
            max_weight = max(max_weight, next[0])
            LOG_weight[next[1]][0] = max_weight

for i in range(1, LOG):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i-1]][i-1]
        LOG_weight[j][i] = max(LOG_weight[j][i-1], LOG_weight[parent[j][i-1]][i-1])

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    maxW = max(LOG_weight[a][LOG - 1], LOG_weight[b][LOG - 1])
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
            maxW = max(maxW, LOG_weight[b][i])
    if a == b:
        return maxW

    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            maxW = max(maxW, LOG_weight[b][i], LOG_weight[b][i])
    return maxW


for u, v, w in input_lines:
    temp = lca(u, v)
    print(temp)
    print(max(sum_weight, sum_weight - temp + w))