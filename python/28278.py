import sys
input = sys.stdin.readline

stk = []
for i in range(int(input())):
    c = input().split()

    if c[0] == '1':
        stk.append(c[1])
    if c[0] == '2':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    if c[0] == '3':
        print(len(stk))
    if c[0] == '4':
        print(abs(int(bool(stk)) - 1))
    if c[0] == '5':
        if stk:
            print(stk[-1])
        else:
            print(-1)