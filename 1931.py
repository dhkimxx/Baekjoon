N = int(input())
if N == 1:
    print(1)
    exit()
timetable = [[*map(int, input().split())] for _ in range(N)]
timetable.sort()
max = 0
for i in range(N):
    end = timetable[i][1]
    count = 1
    test = [timetable[i]]
    for j in range(i + 1, N):
        if timetable[j][0] < end:
            continue
        else:
            end = timetable[j][1]
            count += 1
            test.append(timetable[j])
    if count > max:
        max = count
print(max)