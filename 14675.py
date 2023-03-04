from collections import deque


def tree(t, k):
    if t == 1:
        if k + 1 <= N:
            start = k + 1
        else:
            start = k - 1
        q = deque([start])
        visited[start] = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if i != k and not visited[i]:
                    visited[i] = 1
                    q.append(i)

        if sum(visited) == N - 1:
            return 'no'
        else:
            return 'yes'

    if t == 2:



N = int(input())
graph = [[] for _ in range(N + 1)]
edge = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

for q in range(int(input())):
    visited = [0] * (N + 1)
    t, k = map(int, input().split())
    print(tree(t, k))


