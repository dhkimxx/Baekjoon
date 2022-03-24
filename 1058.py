import sys

N = int(sys.stdin.readline())
graph = []
for n in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

count = [0] * N
for c in range(N):
    count[c] = graph[c].count('Y')
    for a in range(N):
        if graph[c][a] == 'Y':
            count[c] += graph[a].count('Y') - 1
print(max(count))