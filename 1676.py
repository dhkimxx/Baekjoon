def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

ans = 0
N_fac = factorial(int(input()))
for i in str(N_fac)[::-1]:
    if i != '0':
        break
    ans += 1
print(ans)