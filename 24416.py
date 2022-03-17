n = int(input())

countFIB = 0
countDP = 0
f = [0] * (n + 1)

def fib(n):
    global countFIB
    if n == 1 or n == 2:
        countFIB += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def dp(n):
    global countDP
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        countDP += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

fib(n)
dp(n)
print(countFIB, countDP)