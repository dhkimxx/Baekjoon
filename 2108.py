N = int(input())

List = []
for _ in range(N):
    List.append(int(input()))
List.sort()

mean = round(sum(List) / N)

if N % 2:
    median = List[(N + 1) // 2 - 1]
else:
    median = (List[N // 2 - 1] + List[N // 2]) / 2

Dic = {}
for i in range(min(List), max(List) + 1):
    Dic[i] = 0
for l in List:
    Dic[l] += 1
modeList = []
maxValue = max(Dic.values())
for i in range(min(List), max(List) + 1):
    if Dic[i] == maxValue:
        modeList.append(i)
if len(modeList) > 1:
    mode = modeList[1]
else:
    mode = modeList[0]

range = List[-1] - List[0]

print(mean)
print(median)
print(mode)
print(range)
