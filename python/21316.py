graph = [[] for _ in range(13)]
visited = [0] * (13)
for _ in range(12):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for v in range(1, 13):
    if len(graph[v]) == 3:
        arr = []
        for nv in graph[v]:
            arr.append(len(graph[nv]))
        if sorted(arr) == [1, 2, 3]:
            print(v)