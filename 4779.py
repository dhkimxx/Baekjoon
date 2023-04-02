def recursive(n, start, end):
    if n == 0:
        return
    cnt = (end - start + 1) // 3
    recursive(n - 1, start, start + cnt - 1)
    for i in range(start + cnt, start + 2 * cnt):
        arr[i] = ' '
    recursive(n - 1, start + 2 * cnt, end)
# 3 9 27
while 1:
    try:
        N = int(input())
        arr = ['-'] * (3 ** N)
        recursive(N, 0, 3 ** N - 1)
        print(''.join(arr))
    except:
        exit(0)
