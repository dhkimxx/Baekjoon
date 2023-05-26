for _ in range(int(input())):
    N = int(input())
    s = []
    for _ in range(2):
        s.append(list(map(int, input().split())) + [0, 0])
    s[1][1] += s[0][0]
    s[0][1] += s[1][0]
    for i in range(2, N + 2):
        s[1][i] += max(s[0][i - 2], s[0][i - 1])
        s[0][i] += max(s[1][i - 2], s[1][i - 1])
    print(max(map(max, s)))



