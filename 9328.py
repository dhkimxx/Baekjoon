from collections import deque

for _ in range(int(input())):
    h, w = map(int, input().split())
    H, W = h + 2, w + 2
    graph = [['.'] * H]
    for _ in range(h):
        graph.append(list('.' + input() + '.'))
    graph.append(['.'] * H)
    visited = [[0] * W for _ in range(H)]
    key = list(input())


