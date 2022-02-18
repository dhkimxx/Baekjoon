N = int(input())
A, B = [list(map(int, input().split())) for _ in range(2)]
A.sort()
B.sort(reverse=True)
sum = 0
for i in range(N):
    sum += A[i] * B[i]
print(sum)