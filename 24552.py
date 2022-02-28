import sys

S = list(sys.stdin.readline().rstrip())
left = 0
right = 0
Sum = 0
for n in range(len(S)):
    if S[n] == '(':
        Sum += 1
        left += 1
    if S[n] == ')':
        Sum -= 1
        right += 1
    if Sum < 0:
        print(right)
        sys.exit()
    if Sum == 0:
        left = 0
print(left)
