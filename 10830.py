import copy
N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = copy.deepcopy(matrix1)

for m in range(M-1):
    matrix = [[0] * N for _ in range(N)]
    for n in range(N):
        for k in range(N):
            for m in range(N):
                matrix[n][k] += matrix1[n][m] * matrix2[m][k]
                matrix[n][k] %= 1000
    matrix1 = copy.deepcopy(matrix)

for i in range(N):
    print(*matrix1[i])
