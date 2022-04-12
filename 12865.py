import copy
N, K = map(int, input().split())
weight = []
value = []
dp = [[]]

for i in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)
    dp[0].append(i)

result = max(value)

for i in range(1, N):
    for j in range(0, N):
        temp = copy.deepcopy(dp[i - 1])
        if j not in temp:
            continue
        temp.remove(j)
        dp.append(temp)

print(dp)

for W in dp:
    SUM = 0
    VAL = 0
    for w in W:
        SUM += weight[w]
        VAL += value[w]
    if SUM <= K:
        result = max(VAL, result)
print(result)