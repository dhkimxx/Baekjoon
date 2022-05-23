from collections import deque


def q_checked_append(x, y, z):
    v = (x, y, z)
    if v not in checked:
        q.append(v)
        checked.append(v)


A, B, C = map(int, input().split())
checked = [(0, 0, C)]
q = deque([(0, 0, C)])
ans = []
while q:
    a, b, c = q.popleft()
    if a == 0:
        ans.append(c)

    if B >= a + b:
        q_checked_append(0, a + b, c)
    else:
        q_checked_append(a + b - B, B, c)
    if C >= a + c:
        q_checked_append(0, b, a + c)
    else:
        q_checked_append(a + c - C, b, C)

    if A >= b + a:
        q_checked_append(a + b, 0, c)
    else:
        q_checked_append(A, a + b - A, c)
    if C >= b + c:
        q_checked_append(a, 0, b + c)
    else:
        q_checked_append(a, b + c - C, C)

    if A >= a + c:
        q_checked_append(a + c, b, 0)
    else:
        q_checked_append(A, b, a + c - A)
    if B >= b + c:
        q_checked_append(a, b + c, 0)
    else:
        q_checked_append(a, B, b + c - B)

print(*sorted(ans))