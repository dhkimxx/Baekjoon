d = {}
ans = []
for _ in range(int(input())):
    a, b = input().split()
    d[a] = b
for key, value in d.items():
    if value == "enter":
        ans.append(key)
print('\n'.join(sorted(ans, reverse=True)))