N = int(input())
t = list(map(int, input().split()))
t.sort()
personalTime = 0
totalTime = 0
for i in t:
    personalTime += i
    totalTime += personalTime
print(totalTime)
