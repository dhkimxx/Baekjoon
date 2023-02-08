def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)


if __name__ == "__main__":
    for _ in range(int(input())):
        cnt = 0
        ans = is_palindrome(input())
        print(ans, cnt)
