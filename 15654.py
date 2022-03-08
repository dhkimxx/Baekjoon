import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


def backtracking(cnt, result):
    if cnt == M:
        print(*result)
    for i in range(N):
        if arr[i] not in result:
            result.append(arr[i])
            backtracking(cnt + 1, result)
            result.remove(arr[i])


backtracking(0, [])