N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def mul(A, B):
    temp_matrix = [[0] * N for _ in range(N)]
    for n in range(N):
        for k in range(N):
            for m in range(N):
                temp_matrix[n][k] += A[n][m] * B[m][k]
                temp_matrix[n][k] %= 1000
    return temp_matrix

def divide(B):
    if B == 1:
        return matrix
    elif B % 2 == 0:
        result = divide(B//2)
        return mul(result, result)
    elif B % 2 == 1:
        result = divide(B//2)
        return mul(mul(result, result), matrix)

for result in divide(M):
    for r in result:
        print(r % 1000, end=' ')
    print()