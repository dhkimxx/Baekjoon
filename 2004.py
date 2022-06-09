def count_2(n):
    cnt = 0
    while n != 0:
        n //= 2
        cnt += n
    return cnt


def count_5(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt


N, M = map(int, input().split())
print(min(count_2(N) - count_2(M) - count_2(N - M),
          count_5(N) - count_5(M) - count_5(N - M)))