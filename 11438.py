from collections import deque
import sys
input = sys.stdin.readline
LOG = 21    # 2^20 = 1,000,000

N = int(input())
graph = [[] for _ in range(N + 1)]
depth = [0] * (N + 1)
parent = [[0] * LOG for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    depth[start] = 1
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if not depth[nv]:
                depth[nv] = depth[v] + 1
                parent[nv][0] = v
                q.append(nv)

def set_parent():
    bfs(1)
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]


set_parent()
M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
