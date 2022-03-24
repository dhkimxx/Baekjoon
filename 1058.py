import copy
import sys

N = int(sys.stdin.readline())
graph = []
for n in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
friends = []
result = [0] * N

for c in range(N):
    friends.append([])
    for a in range(N):
        if graph[c][a] == 'Y':
            friends[c].append(a)
    result[c] = len(friends[c])

for c in range(N):
    for a_friends in friends[c]:
        for b_friends in friends[a_friends]:
            if b_friends != c and b_friends not in friends[c]:
                result[c] += 1

print(max(result))