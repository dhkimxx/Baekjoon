N = int(input())

number = [True] * (N + 1)
for i in range(2, N + 1):
    if number[i]:
        for j in range(i + i, N + 1, i):
            number[j] = False


prime_number = []
for i in range(2, N + 1):
    if number[i]:
        prime_number.append(i)

cnt = 0
sum_prime = sum(prime_number)
left, right = 0, len(prime_number) - 1
while left <= right:
    if N == sum_prime:
        cnt += 1
    if sum_prime >= N:
        sum_prime -= prime_number[right]
        right -= 1
    if sum_prime < N:
        sum_prime -= prime_number[left]
        left += 1
        right += 1
        if right == len(prime_number):
            break
        sum_prime += prime_number[right]
print(cnt)
