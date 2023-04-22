N, M = map(int, input().split())
dic = {}

for _ in range(N):
    team = input()
    member = [input() for _ in range(int(input()))]
    dic[team] = member
    for m in member:
        dic[m] = team

for _ in range(M):
    q = input()
    if int(input()):
        print(dic[q])
    else:
        print('\n'.join(sorted(dic[q])))
