N, M = map(int, input().split())
dictionary = {}
for _ in range(N):
    dictionary[input()] = 1

ans = 0
for _ in range(M):
    ans += dictionary.get(input(), 0)
print(ans)