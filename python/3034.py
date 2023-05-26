N, W, H = map(int, input().split())
for _ in range(N):
    length = int(input())
    if length <= (W ** 2 + H ** 2) ** 0.5:
        print('DA')
    else:
        print('NE')