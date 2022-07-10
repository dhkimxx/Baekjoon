N, M = int(input()), int(input())
P = list(map(int, input().split()))
passward = [0] * (N + 1)
for p in P:
    passward[p] = 1
graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for i in range(0, N + 1):
    for j in range(i + 1, N + 1):
        if passward[i] and passward[j]:
            graph[i][j] = sum(list(map(int, bin(i ^ j)[2:])))
            print(graph[i][j])