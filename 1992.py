N = int(input())
graph = [list(map(int, input()) ) for _ in range(N)]

def divide(length, x, y):
    start = graph[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if start != graph[i][j]:
                print('(', end='')
                divide(length // 2, x, y)
                divide(length // 2, x, y + length // 2)
                divide(length // 2, x + length // 2, y)
                divide(length // 2, x + length // 2, y + length // 2)
                print(')', end='')
                return
    print(start, end='')

divide(N, 0, 0)