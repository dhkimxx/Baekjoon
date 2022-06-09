for _ in range(int(input())):
    dictionary = {}
    N = int(input())
    for _ in range(N):
        a, b = input().split()
        if not dictionary.get(b, 0):
            dictionary[b] = 1
        else:
            dictionary[b] += 1
    ans = 1
    for key in dictionary:
        ans *= dictionary[key] + 1
    print(ans - 1)