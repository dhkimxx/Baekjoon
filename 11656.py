s = input()
ls = []
for i in range(len(s)):
    ls.append(s[i:])
print('\n'.join(sorted(ls)))