graph = []
blank_cnt = 0
blank = []
for i in range(9):
    graph.append(list(map(int, input())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))
            blank_cnt += 1


def dfs(cnt):
    if cnt == blank_cnt:
        for i in range(9):
            print(''.join(map(str, graph[i])))
        exit()
    x, y = blank[cnt]
    candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if graph[x][i] in candidates:
            candidates.remove(graph[x][i])
        if graph[i][y] in candidates:
            candidates.remove(graph[i][y])
    for i in range(x // 3 * 3, x // 3 * 3 + 3):
        for j in range(y // 3 * 3, y // 3 * 3 + 3):
            if graph[i][j] in candidates:
                candidates.remove(graph[i][j])
    for candidate in candidates:
        graph[x][y] = candidate
        dfs(cnt + 1)
        graph[x][y] = 0

dfs(0)