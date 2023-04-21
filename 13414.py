K, L = map(int, input().split())
dic = {}
for _ in range(L):
    a = input()
    if dic.get(a, 0):
        dic.pop(a)
        dic[a] = 1
    else:
        dic[a] = 1
print('\n'.join(list(dic.keys())[:K]))