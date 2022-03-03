import sys

N, M, B = map(int, sys.stdin.readline().split())
blocks = []
for n in range(N):
    blocks = blocks + list(map(int, sys.stdin.readline().split()))
Min = min(blocks)
Max = max(blocks)
minTime = N * M * 256 * 2
maxLevel = 0
for level in range(Min, Max + 1):
    inventory = B
    timer = 0
    for blk in blocks:
        if blk < level:
            inventory -= level - blk
            timer += level - blk
        if blk > level:
            inventory += blk - level
            timer += 2 * (blk - level)
    if inventory >= 0 and minTime >= timer:
        minTime = timer
        maxLevel = level
print(minTime, maxLevel)
