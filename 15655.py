import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


def backtracking(cnt, result):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        if len(result) > 0 and arr[i] > result[-1] or len(result) == 0:
            result.append(arr[i])
            backtracking(cnt + 1, result)
            result.remove(arr[i])


backtracking(0, [])
