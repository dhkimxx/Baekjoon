import sys

S = list(sys.stdin.readline().rstrip())
left = 0
right = 0
Sum = 0

for n in range(len(S)):
    if S[n] == '(':
        Sum += 1
        left += 1
        if n == len(S) - 1:
            print(1)
            sys.exit()
        if Sum == 2 and n != len(S) - 1:
            left = 1

    if S[n] == ')':
        Sum -= 1
        right += 1
        if n == 0:
            print(1)
            sys.exit()
        if Sum == -2:
            print(right - 1)
            sys.exit()

if Sum == 0:
    print(0)
else:
    print(left)