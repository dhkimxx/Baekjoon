import heapq
import sys
input = sys.stdin.readline
LOG = 18

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inputs = []
for _ in range(M):
    u, v, w = map(int, input().split())
    inputs.append((u, v, w))
    graph[u].append((w, v))
    graph[v].append((w, u))

depth = [0] * (N + 1)
parent = [[0] * LOG for _ in range(N + 1)]
mst_sum_weight = 0
dp = [[0] * LOG for _ in range(N + 1)]
q = [(0, 1, 0)]
cnt = 0
while q and cnt < N:
    weight, now, last = heapq.heappop(q)
    if not depth[now]:
        depth[now] = depth[last] + 1
        mst_sum_weight += weight
        cnt += 1
        parent[now][0] = last
        dp[now][0] = weight
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1], now))

for i in range(1, LOG):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i-1]][i-1]
        dp[j][i] = max(dp[j][i-1], dp[parent[j][i-1]][i-1])


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    max_weight = 0
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            max_weight = max(max_weight, dp[b][i])
            b = parent[b][i]
    if a == b:
        return max_weight
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            max_weight = max(max_weight, dp[b][i], dp[a][i])
            a = parent[a][i]
            b = parent[b][i]
    return max(max_weight, dp[a][0], dp[b][0])


for u, v, w in inputs:
    print(mst_sum_weight - lca(u, v) + w)