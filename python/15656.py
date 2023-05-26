import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


def backtracking(cnt, result):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        result.append(arr[i])
        backtracking(cnt + 1, result)
        result.pop()


backtracking(0, [])
