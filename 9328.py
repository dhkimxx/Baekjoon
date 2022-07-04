from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    H, W = h + 2, w + 2
    graph = [['.'] * H]
    for _ in range(h):
        graph.append(list('.' + input() + '.'))
    graph.append(['.'] * H)
    visited = [[0] * W for _ in range(H)]
    key = list(input())

    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if 97 <= ord(graph[x][y]) <= 122:
            if graph[x][y] not in key:
                key.append(graph[x][y])




# . . . . . . . . . . . . . . . . . . .
# . * * * * * * * * * * * * * * * * * .
# . . . . . . . . . . . . . . * * $ * .
# . * B * A * P * C * * X * Y * . X . .
# . * y * x * a * p * * $ * $ * * $ * .
# . * * * * * * * * * * * * * * * * * .
# . . . . . . . . . . . . . . . . . . .