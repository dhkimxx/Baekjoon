from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    H, W = h + 2, w + 2
    graph = [['.'] * W, ['.'] * W]
    for _ in range(h):
        graph.insert(1, list('.' + input() + '.'))
    key = list(input())
    q = deque([(0, 0)])
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    while q:
        x, y = q.popleft()
        if 97 <= ord(graph[x][y]) <= 122:
            if graph[x][y] not in key:
                key.append(graph[x][y])
                q = deque([(0, 0)])
                visited = [[0] * W for _ in range(H)]
                cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] != '*' and not visited[nx][ny]:
                    if 65 <= ord(graph[nx][ny]) <= 90:
                        if chr(ord(graph[nx][ny]) + 32) not in key:
                            continue
                    if graph[nx][ny] == '$':
                        cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    print(cnt)
# from collections import deque
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for _ in range(int(input())):
#     H, W = map(int, input().split())
#     graph = [list(input()) for _ in range(H)]
#     start = []
#     for h in range(H):
#         for w in range(W):
#             if h % (H - 1) == 0 or w % (W - 1) == 0:
#                 if graph[h][w] != '*':
#                     start.append((h, w))
#     key = list(input())
#     q = deque(start)
#     visited = [[0] * W for _ in range(H)]
#     cnt = 0
#     while q:
#         x, y = q.popleft()
#         if 65 <= ord(graph[x][y]) <= 90:
#             if chr(ord(graph[x][y]) + 32) not in key:
#                 continue
#         if graph[x][y] == '$' and not visited[x][y]:
#             visited[x][y] = 1
#             cnt += 1
#         if 97 <= ord(graph[x][y]) <= 122:
#             if graph[x][y] not in key:
#                 key.append(graph[x][y])
#                 q = deque(start)
#                 visited = [[0] * W for _ in range(H)]
#                 cnt = 0
#
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < H and 0 <= ny < W:
#                 if graph[nx][ny] != '*' and not visited[nx][ny]:
#                     if 65 <= ord(graph[nx][ny]) <= 90:
#                         if chr(ord(graph[nx][ny]) + 32) not in key:
#                             continue
#                     if graph[nx][ny] == '$':
#                         cnt += 1
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#     print(cnt)