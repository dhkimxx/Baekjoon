from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))
target = sorted(arr)


def bfs():
    checked = {str(arr): 0}
    q = deque([arr])
    while q:
        now_arr = q.popleft()
        if now_arr == target:
            return checked[str(now_arr)]
        for i in range(0, N - K + 1):
            new_arr = now_arr[:i] + list(reversed(now_arr[i:i+K])) + now_arr[i+K:]
            if not checked.get(str(new_arr), 0):
                checked[str(new_arr)] = checked[str(now_arr)] + 1
                q.append(new_arr)
                print(new_arr)
    return -1


print(bfs())