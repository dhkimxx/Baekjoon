N, F = int(input()), int(input())
result = 100
for n in range(N // 100 * 100, N // 100 * 100 + 100):
    if n % F == 0 and n % 100 < result:
        result = n % 100
if result < 10:
    print(0,end="")
print(result)