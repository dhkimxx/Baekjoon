ans = 0
_set = set()
for _ in range(int(input())):
    a = input()
    if a == "ENTER":
        ans += len(_set)
        _set = set()
    else:
        _set.add(a)
else:
    ans += len(_set)
print(ans)