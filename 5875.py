S = list(input())
left = 0
right = 0
Sum = 0
for n in range(len(S)):
    if S[n] == '(':
        Sum += 1
        left += 1
    else:
        Sum -= 1
        right += 1
    if Sum < 2:
        left = 0
    if Sum == -1:
        print(right)
        exit()
if Sum == 0:
    print(0)
else:
    print(left)