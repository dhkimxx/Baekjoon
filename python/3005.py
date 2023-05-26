R, C = map(int, input().split())
graph = [input() for _ in range(R)]
graph_T = list(zip(*graph))
ans = []
for line in graph + graph_T:
    words = ''.join(list(line)).split('#')
    for word in words:
        if len(word) > 1:
            ans.append(word)
print(min(ans))
# R, C = map(int, input().split())
# graph = []
# for r in range(R):
#     graph.append(list(input()))
#
#
# def dfs_r(x, y, log):
#     visited_r[x][y] = 1
#     nx, ny = x + 1, y
#     if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#':
#         return dfs_r(nx, ny, log + graph[nx][ny])
#     return log
#
#
# def dfs_c(x, y, log):
#     visited_c[x][y] = 1
#     nx, ny = x, y + 1
#     if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#':
#         return dfs_c(nx, ny, log + graph[nx][ny])
#     return log
#
#
# visited_r = [[0] * C for _ in range(R)]
# visited_c = [[0] * C for _ in range(R)]
# ans = ''
# for i in range(R):
#     for j in range(C):
#         if graph[i][j] != '#':
#             if not visited_c[i][j]:
#                 word = dfs_c(i, j, graph[i][j])
#                 if len(word) >= 2:
#                     if ans == '':
#                         ans = word
#                     else:
#                         ans = min(ans, word)
#             if not visited_r[i][j]:
#                 word = dfs_r(i, j, graph[i][j])
#                 if len(word) >= 2:
#                     if ans == '':
#                         ans = word
#                     else:
#                         ans = min(ans, word)
# print(ans)