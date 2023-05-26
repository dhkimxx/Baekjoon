def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

A, B = map(int, input().split())
if A < B:
    A, B = B, A
gcd = GCD(A, B)
print(gcd)
print(A * B // gcd)