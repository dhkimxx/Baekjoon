N, M = map(int, input().split())
dictionary = {}
for _ in range(N):
    dictionary[input()] = 1
ans = []
for _ in range(M):
    temp = input()
    if dictionary.get(temp, 0):
        ans.append(temp)
print(len(ans))
print('\n'.join(sorted(ans)))
