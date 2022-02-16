N = int(input())
timeList = []
personalTime = 0
totalTime = 0
for i in range(0, int(N)):
    t = int(input())
    timeList.append(t)
timeList.sort()
for i in timeList:
    personalTime += i
    totalTime += personalTime
print(totalTime)
