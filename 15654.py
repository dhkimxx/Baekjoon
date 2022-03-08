import sys

N, M = map(int, sys.stdin.readline().split())
Nums = list(sys.stdin.readline().split())
Nums.sort()


def backtracking(cnt, result):
    print(cnt, result)
    if cnt == M:
        print(' '.join(result))
    temp = result.copy()
    for i in range(cnt, M):
        result.append(Nums[i])
        backtracking(cnt + 1, result)
        result = temp


backtracking(0, [])
