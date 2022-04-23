import sys


def find_part_sum(arr, arr_part_sum, index, now_sum):
    if index == len(arr):
        arr_part_sum.append(now_sum)
        return
    find_part_sum(arr, arr_part_sum, index + 1, now_sum)
    find_part_sum(arr, arr_part_sum, index + 1, now_sum + arr[index])


N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
front = arr[:N // 2]
back = arr[N // 2:]
front_part_sum = []
back_part_sum = []
find_part_sum(front, front_part_sum, 0, 0)
find_part_sum(back, back_part_sum, 0, 0)
front_part_sum = front_part_sum
back_part_sum = back_part_sum
back_part_sum.sort()    # sorting for binary search

print(front_part_sum, back_part_sum)
cnt = 0
for i in front_part_sum:
    left = 0
    right = len(back_part_sum) - 1
    target = S - i

    start = 0
    end = len(back_part_sum) - 1
    while end - start >= 0:
        mid = (start + end) // 2
        if back_part_sum[mid] <= target:
            start = mid + 1
            if back_part_sum[mid] == target:
                right = mid
        if back_part_sum[mid] > target:
            end = mid - 1

    start = 0
    end = len(back_part_sum) - 1
    while end - start >= 0:
        mid = (start + end) // 2
        if back_part_sum[mid] < target:
            start = mid + 1
        if back_part_sum[mid] >= target:
            end = mid - 1
            if back_part_sum[mid] == target:
                left = mid
    if back_part_sum[left] == back_part_sum[right]:
        cnt += right - left + 1
        print(i,':' , left, right)
if S == 0:
    cnt -= 1
print(cnt)
