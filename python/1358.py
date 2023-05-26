W, H, X, Y, P = map(int, input().split())
ans = 0
for _ in range(P):
    Px, Py = map(int, input().split())
    if X <= Px <= X + W and Y <= Py <= Y + H:
        ans += 1
    elif (Px - X) ** 2 + (Py - Y - H / 2) ** 2 <= (H / 2) ** 2:
        ans += 1
    elif (Px - X - W) ** 2 + (Py - Y - H / 2) ** 2 <= (H / 2) ** 2:
        ans += 1
print(ans)