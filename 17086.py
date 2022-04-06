import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
for n in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 1, -1, 0, 0]

def bfs(start):
    queue = deque([start])


