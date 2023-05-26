N = list(map(str, input()))
N.sort(reverse=True)
if '0' not in N:
    print(-1)
    exit()
else:
    Num = int(''.join(N))
    if Num % 30 == 0:
        print(Num)
    else:
        print(-1)