# def dfs(output, res, level):
#     if level == N :
#         if res == 0:
#             print(output)
#             return
#     else:
#         next_output = output + ' ' + str(a[level])
#         if level == 1:
#             next_res = 10 * a[level - 1] + a[level]
#             dfs(next_output, next_res, level + 1)
#         else:
#             if output[-2] == '+':
#                 next_res = res - a[level - 1] + 10 * a[level - 1] + a[level]
#                 dfs(next_output, next_res, level + 1)
#             if output[-2] == '-':
#                 next_res = res + a[level - 1] - 10 * a[level - 1] - a[level]
#                 dfs(next_output, next_res, level + 1)
#
#         next_output = output + '+' + str(a[level])
#         next_res = res + a[level]
#         dfs(next_output, next_res, level + 1)
#
#         next_output = output + '-' + str(a[level])
#         next_res = res - a[level]
#         dfs(next_output, next_res, level + 1)
#
#
# for _ in range(int(input())):
#     N = int(input())
#     a = [i for i in range(1, N + 1)]
#     output = '1'
#     dfs(output, 1, 1)
#     print()

def dfs(output, level):
    if len(output) == 2 * N - 1:
        if eval(output.replace(' ','')) == 0:
            print(output)
    else:
        dfs(output + ' ' + str(level + 1), level + 1)
        dfs(output + '+' + str(level + 1), level + 1)
        dfs(output + '-' + str(level + 1), level + 1)


for _ in range(int(input())):
    N = int(input())
    output = '1'
    dfs(output, 1)
    print()