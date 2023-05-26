T = int(input())
button = [5*60, 1*60, 10]
count = [0, 0, 0]
for i in range(3):
    count[i] = T // button[i]
    T %= button[i]
if T != 0:
    print(-1)
else:
    print(count[0], count[1], count[2])