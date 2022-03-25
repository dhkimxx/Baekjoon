import sys

N = int(sys.stdin.readline())
graph = []
visited = [[0] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == 'Y':
                visited[i][j] = 1
            if graph[i][k] == 'Y' and graph[k][j] == 'Y':
                visited[i][j] = 1

result = 0
for i in range(N):
    result = max(sum(visited[i]), result)
print(result)
'''
import sys

N = int(sys.stdin.readline())
graph = []
for n in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

friends = []
result = []

for c in range(N):
    friends.append([])
    result.append([])
    for a in range(N):
        if graph[c][a] == 'Y':
            friends[c].append(a)
            result[c].append(a)

max = 0
for c in range(N):
    for a_friends in friends[c]:
        for b_friends in friends[a_friends]:
            if b_friends != c and b_friends not in result[c]:
                result[c].append(b_friends)
    if len(result[c]) > max:
        max = len(result[c])
print(max)
'''