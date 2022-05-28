from collections import deque
import sys
input = sys.stdin.readline
LOG = 21 # 2^20 = 1,000,000

N = int(input())
graph = [[] for _ in range(N + 1)]
depth = [0] * (N + 1)
parent = [0] * (N + 1)
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
                parent[nv] = v
                q.append(nv)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a


bfs(1)
M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
