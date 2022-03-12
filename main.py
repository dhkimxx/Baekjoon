N = input()
result = 0
for n in range(len(N)):
    if ord(N[n]) <= 57:
        result += N[n] * 16 ** (len(N) - n - 1)
    else:
        result += (ord(N[n]) - 55) * 16 ** (len(N) - n - 1)
print(result)
print(int(N, 16))