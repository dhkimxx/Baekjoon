def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    gcd = GCD(A, B)
    print(A * B // gcd)