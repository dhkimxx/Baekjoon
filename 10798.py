a = []
for _ in range(5):
    s = input()
    s += '*' * (15 - len(s))
    a.append(s)
for i in list(zip(*a)):
    print(''.join(list(i)).replace('*',''), end='')