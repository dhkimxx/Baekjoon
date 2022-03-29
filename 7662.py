import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    arr = []
    for _ in range(int(sys.stdin.readline())):
        Q, N = list(sys.stdin.readline().split())
        if Q == 'I':
            arr.append(int(N))

        if Q == 'D' and len(arr) != 0:
            arr.sort()
            if N == '1':
                arr.pop()
            if N == '-1':
                arr.pop(0)
    if len(arr) == 0:
        print('EMPTY')
    else:
        print(arr[-1], arr[0])