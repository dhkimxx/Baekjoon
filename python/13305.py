N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
minCost = 1000000001
totalCost = 0
for i in range(N - 1):
    if cost[i] < minCost:
        minCost = cost[i]
    totalCost += distance[i] * minCost
print(totalCost)