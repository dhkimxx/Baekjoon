def merge_sort(start, end):
    global K
    if start == end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    if K <= end - start + 1:
        s = sorted(A[start:end+1])
        print(s[K-1])
        exit()
    K -= end - start + 1


N, K = map(int, input().split())
A = list(map(int, input().split()))
merge_sort(0, N - 1)
print(-1)