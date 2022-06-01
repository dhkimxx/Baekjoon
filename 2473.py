N = int(input())
arr = sorted(list(map(int, input().split())))
ans = []
MIN = 1e12
for n in range(N-2):
    left = n + 1
    right = N - 1
    while left < right:
        SUM = arr[n] + arr[left] + arr[right]
        if abs(SUM) < abs(MIN):
            MIN = SUM
            ans = [arr[n], arr[left], arr[right]]
        if SUM > 0:
            right -= 1
        else:
            left += 1
print(*ans)