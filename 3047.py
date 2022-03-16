num = list(map(int, input().split()))
order = input()
num.sort()
for output in order:
    if output == 'A':
        print(num[0], end=" ")
    if output == 'B':
        print(num[1], end=" ")
    if output == 'C':
        print(num[2], end=" ")
