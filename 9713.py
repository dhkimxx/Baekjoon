for _ in range(int(input())):
    ans = 0
    a = int(input())
    for i in range(1, a + 1):
        if i % 2:
            ans += i
    print(ans)