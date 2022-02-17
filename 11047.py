N,K = map(int, input().split())
result = 0
coin = []
for i in range(N):
    coin.append(int(input().strip()))
coin.sort(reverse=True)
i = 0
while True:
    if coin[i] < K:
        result = result + K // coin[i]
        K = K % coin[i]
    i += 1
    if i >= N:
        break
print(result)