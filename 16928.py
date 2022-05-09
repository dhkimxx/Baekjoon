from collections import deque

N, M = map(int, input().split())
ladder = [0] * 101
snake = [0] * 101
visited = [0] * 101
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b

q = deque([1])
visited[1] = 1
while q:
    v = q.popleft()
    for dice_number in [1, 2, 3, 4, 5, 6]:
        nv = v + dice_number
        if nv > 100:
            continue
        if ladder[nv]:
            nv = ladder[nv]
        if snake[nv]:
            nv = snake[nv]
        if not visited[nv]:
            visited[nv] = visited[v] + 1
            q.append(nv)
print(visited[100] - 1)