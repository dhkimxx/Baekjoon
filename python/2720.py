for _ in range(int(input())):
    a = int(input())
    for i in [25, 10, 5, 1]:
        print(a // i, end=' ')
        a %= i
    print()