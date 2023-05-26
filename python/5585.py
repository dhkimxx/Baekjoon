N = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
count = 0
for i in coin:
    count += N // i
    N %= i
print(count)