S = int(input())
cnt = 0
Sum = 0
while 1:
    cnt += 1
    Sum += cnt
    if Sum > S:
        print(cnt - 1)
        exit()