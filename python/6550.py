while 1:
    try:
        s, t = map(str, input().split())
        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                j += 1
        if j == len(s):
            print('Yes')
        else:
            print('No')
    except:
        break