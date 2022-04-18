S = list(input())
count = [[0] * 26 for _ in range(len(S) + 1)]
for i in range(1, len(S) + 1):
    count[i] = count[i - 1]
    count[i][ord(S[i - 1]) - 97] += 1
    print('i = ',i, count[i])
for _ in range(int(input())):
    temp = input().split()
    a, l, r = temp[0], int(temp[1]) + 1, int(temp[2]) + 1
    print(ord(a) - 97, l, r)
    print(count[r][ord(a) - 97] - count[l - 1][ord(a) - 97])
