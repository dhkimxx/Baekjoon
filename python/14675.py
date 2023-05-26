import sys
input = sys.stdin.readline
N = int(input())
graph = [0] * (N + 1)

for n in range(N - 1):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1

for q in range(int(input())):
    t, k = map(int, input().split())
    res = 'yes'
    if t == 1 and graph[k] == 1:
        res = 'no'
    print(res)
