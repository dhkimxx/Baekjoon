N, M = map(int, input().split())
a = [i for i in range(1, N + 1)]
for m in range(M):
    i, j = map(int, input().split())
    a[i-1:j] = reversed(a[i-1:j])
print(*a)