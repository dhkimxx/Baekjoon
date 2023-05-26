import sys
N, M = map(int, sys.stdin.readline().split())
wood = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(wood)
mid = (start + end) // 2
maxH = 0
while end - start >= 0:
    Sum = 0
    for w in wood:
        if w > mid:
            Sum += w - mid
    if Sum == M:
        print(mid)
        sys.exit()
    if Sum < M:
        end = mid - 1
    if Sum > M:
        start = mid + 1
        maxH = mid
    mid = (start + end) // 2
print(maxH)
