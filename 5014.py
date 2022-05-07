from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)


def bfs(s):
    q = deque([s])
    visited[s] = 1
    while q:
        v = q.popleft()
        for nv in [v + U, v - D]:
            if 1 <= nv <= F and not visited[nv]:
                q.append(nv)
                visited[nv] = visited[v] + 1


bfs(S)
if visited[G]:
    print(visited[G] - 1)
else:
    print("use the stairs")