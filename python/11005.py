N, B = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = []
while N:
    res.append(N % B)
    N //= B
for i in res[::-1]:
    print(number[i], end='')
