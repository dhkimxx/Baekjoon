N, B = map(int, input().split())
P = []
for n in range(N):
    p, s = map(int, input().split())
    count = p + s
    discount = p / 2 + s
    P.append((count, discount))
P.sort(key=lambda x:x[0])
ans = 0
for i in range(N):
    tmp = B
    tmp -= P[i][1]
    cnt = 0
    if tmp >= 0:
        cnt += 1
        for j in range(N):
            if i != j:
                tmp -= P[j][0]
                if tmp >= 0:
                    cnt += 1
                else:
                    break
    ans = max(ans, cnt)
print(ans)
