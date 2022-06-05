def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
for _ in range(M):
    Q, a, b = map(int, input().split())
    if Q:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
    else:
        union_parent(a, b)
