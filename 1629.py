A, B, C = map(int, input().split())


def divide(B):
    if B == 1:
        return A % C
    if B % 2 == 0:
        return divide(B//2) ** 2 % C
    if B % 2 == 1:
        return A * (divide(B//2) ** 2) % C


print(divide(B))