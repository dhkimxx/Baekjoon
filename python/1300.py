N, K = int(input()), int(input())
start = 1
end = N * N
result = 0
while end - start >= 0:
    mid = (start + end) // 2
    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)
    if count < K:
        start = mid + 1
    if count >= K:
        result = mid
        end = mid - 1
print(result)