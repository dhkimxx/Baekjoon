N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sumLevel = 0
notInView = 0
for n in range(N):
    if B[n] == 0:
        notInView += A[n]
    sumLevel += A[n]
print(f"{sumLevel}\n{notInView}")
