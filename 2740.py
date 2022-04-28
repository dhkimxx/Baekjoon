N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(M)]
for n in range(N):
    for k in range(K):
        result = 0
        for m in range(M):
            result += matrix1[n][m] * matrix2[m][k]
        print(result, end=' ')
    print()
