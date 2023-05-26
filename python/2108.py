import sys

N = int(sys.stdin.readline())

List = []
for _ in range(N):
    List.append(int(sys.stdin.readline()))
List.sort()

mean = round(sum(List) / N)
median = List[(N + 1) // 2 - 1]

Dic = {}
Min = min(List)
Max = max(List)
for i in range(Min, Max + 1):
    Dic[i] = 0
for l in List:
    Dic[l] += 1
modeList = []
maxValue = max(Dic.values())
for i in range(Min, Max + 1):
    if Dic[i] == maxValue:
        modeList.append(i)
if len(modeList) > 1:
    mode = modeList[1]
else:
    mode = modeList[0]

range = List[-1] - List[0]

print(f"{mean}\n{median}\n{mode}\n{range}")
