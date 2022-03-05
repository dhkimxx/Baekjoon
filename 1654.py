import sys

K, N = map(int, sys.stdin.readline().split())
cables = []
for k in range(K):
    cables.append(int(sys.stdin.readline()))

start = 1
end = max(cables)
mid = (start + end) // 2
maxLength = 0
while end - start >= 0:
    count = 0
    for cable in cables:
        count += cable // mid
    if N <= count:
        maxLength = mid
        start = mid + 1
    if N > count:
        end = mid - 1
    mid = (start + end) // 2

print(maxLength)
