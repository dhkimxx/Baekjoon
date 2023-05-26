N = int(input())
timetable = []
for i in range(N):
    meeting = {}
    meeting['start'], meeting['end'] = map(int, input().split())
    timetable.append(meeting)
    for j in range(i):
        if timetable[j]['start'] == timetable[i]['start']:
            if timetable[j]['end'] < timetable[i]['end']:
                timetable.pop()
                i -= 1
                j -= 1
                N -= 1
        if timetable[j]['start'] > timetable[i]['start']:
            timetable[j], timetable[i] = timetable[i], timetable[j]

max = 0
for i in range(0,N):
    end = 0
    count = 0
    for j in range(j,N):
        if timetable[j]['start'] < end:
            break
        else:
            end = timetable[j]['end']
            count += 1
    if count > max:
        max = count
print(max)