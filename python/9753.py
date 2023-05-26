def prime_list(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        for j in range(i+i, n + 1, i):
            sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i] == True]


primes = prime_list(100000)
for t in range(int(input())):
    K = int(input())
    flag = 1
    while flag:
        for prime in primes:
            if K % prime == 0 and (K // prime) in primes and prime != (K // prime):
                print(K)
                flag = 0
                break
        if flag:
            K += 1
