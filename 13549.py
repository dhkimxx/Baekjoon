from collections import deque

N, K = map(int, input().split())
visited = [1e9] * 100001


def bfs(start, end):
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for nv in [v - 1, v + 1]:
            if 0 <= nv <= 100000 and visited[nv] > visited[v] + 1:
                visited[nv] = visited[v] + 1
                q.append(nv)
        nv = 2 * v
        if 0 <= nv <= 100000 and visited[nv] > visited[v]:
            visited[nv] = visited[v]
            q.append(nv)

    return visited[end] - 1


print(bfs(N, K))
