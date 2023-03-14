N = int(input())
P = list(map(int, input().split()))

for i in range(N):
    for j in range(i + 1, N):
        P[j] = max(P[j], P[i] + P[j-i-1])
print(P[-1])