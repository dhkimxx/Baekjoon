N, S = map(int, input().split())
arr = list(map(int, input().split()))
SUM = sum(arr)
left = 0
right = N - 1
result = 0
while left <= right:
    if SUM >= S:
        SUM -= arr[right]
        result = right - left + 1
        right -= 1
    else:
        SUM -= arr[left]
        left += 1
        right += 1
        if right == N:
            break
        SUM += arr[right]
print(result)
