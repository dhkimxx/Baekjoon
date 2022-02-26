A, B = map(int, input().split())
if A < B:
    A, B = B, A
for n in range(B, 0, -1):
    if B % n == 0 and A % n == 0:
        print(n)
        break
for n in range(B, A * B + 1):
    if n % B == 0 and n % A == 0:
        print(n)
        break