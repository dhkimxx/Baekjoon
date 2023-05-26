import sys
N = int(sys.stdin.readline())
timeTable = []
for n in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    dic = {'T_i': temp[0], 'S_i': temp[1]}
    timeTable.append(dic)
sortedTimeTable = sorted(timeTable, key=lambda x: x['S_i'])
end = 0
start = []
for t in sortedTimeTable:
    end += t['T_i']
    start.append(t['S_i'] - end)
    if end > t['S_i']:
        print(-1)
        exit()
print(min(start))
