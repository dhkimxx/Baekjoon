def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


N = int(input())
start, *ring = list(map(int, input().split()))
for r in ring:
    if r < start:
        gcd = GCD(start, r)
    else:
        gcd = GCD(r, start)
    print(f'{start//gcd}/{r//gcd}')
