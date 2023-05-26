import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0] * (N + 1)]
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    arr.append([0] + list(map(int, input().split())))
for i in range(0, N):
    for j in range(0, N):
        dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + arr[i + 1][j + 1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])

# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# arr = [[0] * (N + 1)]
# for i in range(1, N + 1):
#     arr.append([0] + list(map(int, input().split())))
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         arr[i][j] = arr[i][j] + arr[i][j - 1]
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         arr[i][j] = arr[i][j] + arr[i - 1][j]
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(arr[x2][y2] - arr[x2][y1 - 1] - arr[x1 - 1][y2] + arr[x1 - 1][y1 - 1])
