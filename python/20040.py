import sys
sys.setrecursionlimit(200000)


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        print(m)
        exit()
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
parent = [i for i in range(N)]
for m in range(1, M + 1):
    a, b = map(int, input().split())
    union_parent(a, b)
print(0)
