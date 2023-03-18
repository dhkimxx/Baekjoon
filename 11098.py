for _ in range(int(input())):
    m = 0
    ans = ''
    for _ in range(int(input())):
        a, b = input().split()
        if int(a) > m:
            m = int(a)
            ans = b
    print(ans)