for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        if ((x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2) ^ ((x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2):
            ans += 1
    print(ans)
