import sys

N, C = map(int, sys.stdin.readline().split())
X = []
for n in range(N):
    X.append(int(sys.stdin.readline()))
X.sort()

start = 1
end = X[-1] - X[0]
maxDistance = 0
while end - start >= 0:
    mid = (start + end) // 2
    count = 1
    temp = X[0] + mid
    for x in X:
        if x >= temp:
            count += 1
            temp = x + mid
    if count >= C:
        maxDistance = mid
        start = mid + 1
    else:
        end = mid - 1

print(maxDistance)