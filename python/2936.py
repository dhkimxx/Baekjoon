r = 250
s = r * r * 0.5
x, y = map(int, input().split())
if x == 0 and y == 0:
    nx = 125
    ny = 125
elif x == 250 and y == 0:
    nx = 0
    ny = 125
elif x == 0 and y == 250:
    nx = 125
    ny = 0
elif x == 0:
    if 0 < y < 125:
        nx = s / (250 - y)
        ny = 250 - nx
    if 125 <= y < 250:
        nx = s / y
        ny = 0
elif y == 0:
    if 0 < x < 125:
        ny = s / (250 - x)
        nx = 250 - ny
    if 125 <= x < 250:
        nx = 0
        ny = s / x
else:
    if x > y:
        nx = 0
        ny = 250 - s / x
    else:
        ny = 0
        nx = 250 - s / y
print(f"{nx:.2f} {ny:.2f}")