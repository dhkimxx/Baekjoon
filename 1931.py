N = int(input())
if N == 1:
    print(1)
    exit()
timetable = [[*map(int, input().split())] for _ in range(N)]
timetable.sort(key=lambda x: [x[1], x[0]])
max = 0
end = 0
count = 0
test = []
for i in range(N):
    if timetable[i][0] == timetable[i][1]:
        end = timetable[i][1]
        count += 1
        test.append(timetable[i])
    elif timetable[i][0] >= end:
        end = timetable[i][1]
        count += 1
        test.append(timetable[i])
    if count > max:
        max = count
print(max)