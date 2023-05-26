from collections import deque
T = int(input())
for t in range(T):
    N, target = map(int, input().split())
    status = list(map(int, input().split()))
    deq = deque()
    deqStatus = deque()
    for n in range(N):
        deq.append(n)
        deqStatus.append(status[n])
    count = 1
    while 1:
        maxStatus = max(deqStatus)
        if deqStatus[0] < maxStatus:
            deqStatus.rotate(-1)
            deq.rotate(-1)
        elif deqStatus[0] == maxStatus:
            deqStatus.popleft()
            if deq[0] == target:
                print(count)
                break
            else:
                count += 1
                deq.popleft()