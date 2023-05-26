arr = [input().split() for _ in range(int(input()))]
arr.sort(key =lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(arr[-1][0]+'\n'+arr[0][0])