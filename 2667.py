import sys
N = int(sys.stdin.readline())
graph = []
for n in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y, cnt):
    if x < 0 or y < 0 or x >= N or y >= N:
        return cnt - 1
    if graph[x][y] == 0:
        return cnt - 1
    if graph[x][y] != 0:
        graph[x][y] = 0
        cnt = dfs(x - 1, y, cnt + 1)
        cnt = dfs(x + 1, y, cnt + 1)
        cnt = dfs(x, y - 1, cnt + 1)
        cnt = dfs(x, y + 1, cnt + 1)
        return cnt

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            result.append(dfs(i, j, 1))

print(len(result))
for r in sorted(result):
    print(r)