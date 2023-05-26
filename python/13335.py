from collections import deque

n, w, l = map(int, input().split())
t = deque(map(int, input().split()))
bridge = deque([0] * w)
ans = 0
while bridge:
    ans += 1
    bridge.popleft()
    if not t:
        continue
    elif sum(bridge) + t[0] <= l:
        bridge.append(t.popleft())
    else:
        bridge.append(0)
print(ans)