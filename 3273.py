N = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
cnt = 0
start = N - 1
for i in range(N):
    for j in range(start, i, -1):
        if arr[j] == x - arr[i]:
            cnt += 1
        if arr[j] < x - arr[i]:
            start = j
            break

print(cnt)