from collections import deque

for _ in range(int(input())):
    N = int(input())
    T = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    inDegree = [0] * (N + 1)

    for i in range(N):
        for j in range(i + 1, N):
            graph[T[i]].append(T[j])
            inDegree[T[j]] += 1

    M = int(input())
    for m in range(M):
        a, b = map(int, input().split())
        if b in graph[a]:
            a, b = b, a
        graph[b].remove(a)
        graph[a].append(b)
        inDegree[b] += 1
        inDegree[a] -= 1

    q = deque()
    for i in range(N):
        if inDegree[T[i]] == 0:
            q.append(T[i])

    ans = []
    while q:
        now = q.popleft()
        ans.append(now)
        for next in graph[now]:
            inDegree[next] -= 1
            if inDegree[next] == 0:
                q.append(next)

    if len(ans) != N:
        print("IMPOSSIBLE")
    else:
        print(*ans)