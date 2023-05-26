N, B = input().split()
N = ''.join(reversed(N))
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0
for n in range(len(N)):
    ans += number.index(N[n]) * (B ** n)
print(ans)
