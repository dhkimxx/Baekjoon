N = int(input())
graph = [0] * (N + 1)
for n in range(1, N + 1):
    graph[n] = int(input())
ans = 0
max_cnt = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    now = i
    cnt = 0
    while not visited[now]:
        visited[now] = 1
        now = graph[now]
        cnt += 1
    if cnt > max_cnt:
        ans = i
        max_cnt = cnt
print(ans)