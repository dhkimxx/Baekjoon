dic = {}
dic["ChongChong"] = 1
for _ in range(int(input())):
    a, b = input().split()
    if dic.get(a, 0):
        dic[b] = 1
    if dic.get(b, 0):
        dic[a] = 1
print(sum(dic.values()))