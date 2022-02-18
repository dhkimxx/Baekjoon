N,K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input().strip()))
coin.sort(reverse=True)
result = 0
for i in range(N):
    if coin[i] <= K:
        result += K // coin[i]
        K %= coin[i]
print(result)