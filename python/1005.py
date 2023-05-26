from collections import deque

for _ in range(int(input())):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    inDegree = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    result = [0] * (N + 1)
    q = deque()
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)
            result[i] = time[i]

    while q:
        now = q.popleft()
        for next in graph[now]:
            inDegree[next] -= 1
            result[next] = max(result[next], result[now] + time[next])
            if inDegree[next] == 0:
                q.append(next)

    print(result[int(input())])
