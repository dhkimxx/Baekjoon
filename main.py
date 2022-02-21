lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temtLst = lst.copy()
n = 0
for i in range(len(lst)):
    lst = temtLst
    for j in range(len(lst)):
        lst[i], lst[j] = lst[j], lst[i]
        n += 1
        print(lst,n)