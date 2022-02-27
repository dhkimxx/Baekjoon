method = str(input())
cup = [1,0,0]
for n in range(len(method)):
    if method[n] == 'A':
        cup[0], cup[1] = cup[1], cup[0]
    if method[n] == 'B':
        cup[2], cup[1] = cup[1], cup[2]
    if method[n] == 'C':
        cup[0], cup[2] = cup[2], cup[0]
for n in range(len(cup)):
    if cup[n] == 1:
        print(n + 1)