while 1:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        exit()
    if A > B:
        print('Yes')
    else:
        print('No')