import sys

N, M = map(int, input().split())
dic = {}
for n in range(N):
    temp = list(sys.stdin.readline().split())
    dic[temp[0]] = temp[1]
for m in range(M):
    print(dic[sys.stdin.readline()[:-1]])
