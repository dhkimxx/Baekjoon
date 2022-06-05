import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_find(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        parent[x] = y
        count[y] += count[x]
    return count[y]


for _ in range(int(input())):
    parent = {}
    count = {}
    for _ in range(int(input())):
        a, b = input().split()
        if not parent.get(a, 0):
            parent[a] = a
            count[a] = 1
        if not parent.get(b, 0):
            parent[b] = b
            count[b] = 1
        print(union_find(a, b))

