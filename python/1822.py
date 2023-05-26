n_a, n_b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dic = {}
for a in A:
    dic[a] = 1
for b in B:
    if dic.get(b, 0):
        dic[b] = 0
ans = []
for key, value in dic.items():
    if value:
        ans.append(key)
print(len(ans))
print(*sorted(ans))
