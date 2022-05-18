from collections import deque

N, M = map(int, input().split())
K_n, *K = list(map(int, input().split()))
checked_person = [0] * (N + 1)
able_party = [1] * M
graph = []
for _ in range(M):
    P_n, *P = list(map(int, input().split()))
    graph.append(P)

q = deque(K)
for k in K:
    checked_person[k] = 1
while q:
    v = q.popleft()
    for m in range(M):
        if v in graph[m]:
            able_party[m] = 0
            for nv in graph[m]:
                if not checked_person[nv]:
                    q.append(nv)
                    checked_person[nv] = 1
print(sum(able_party))