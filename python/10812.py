N, M = map(int, input().split())
a = [i for i in range(1, N + 1)]
for m in range(M):
    i, j, k = map(int, input().split())
    a[i - 1:j] = a[k - 1: j] + a[i - 1: k - 1]
print(*a)