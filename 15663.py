import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


def backtracking(cnt, result):
    temp = -1
    if cnt == M:
        for r in result:
            print(arr[r], end=" ")
        print()
        return
    for i in range(N):
        if temp != arr[i] and i not in result:
            result.append(i)
            backtracking(cnt + 1, result)
            temp = arr[result.pop()]


backtracking(0, [])
