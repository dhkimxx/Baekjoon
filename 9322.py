for _ in range(int(input())):
    N = int(input())
    key1 = list(input().split())
    key2 = list(input().split())
    target = list(input().split())

    dic = {}
    res = [''] * N
    for n in range(N):
        dic[n] = key1.index(key2[n])
        res[dic[n]] = target[n]
    print(*res)