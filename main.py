T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    result = 1
    for _ in range(b):
        result = result * a % 10
    if result == 0:
        print(10)
    else:
        print(result)