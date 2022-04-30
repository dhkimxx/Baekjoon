N = int(input())
if N == 1:
    print(N)
    exit()

def mul(A, B):
    temp_matrix = [[0] * 2 for _ in range(2)]
    for n in range(2):
        for k in range(2):
            for m in range(2):
                temp_matrix[n][k] += A[n][m] * B[m][k]
                temp_matrix[n][k] %= 1000000007
    return temp_matrix


ans = [[1, 0], [0, 1]]
a = [[1, 1], [1, 0]]

while(N > 0):
    if N % 2 == 1:
        ans = mul(ans, a)
    a = mul(a, a)
    N //= 2

print(ans[0][1])