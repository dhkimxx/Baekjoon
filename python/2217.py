N = int(input())
rope = []
for _ in range(N):
    W = int(input())
    rope.append(W)
rope.sort(reverse=True)
weightMax = 0
for _ in range(N):
    localMax = len(rope) * rope[-1]
    rope.pop()
    if localMax >= weightMax:
        weightMax = localMax
print(weightMax)
