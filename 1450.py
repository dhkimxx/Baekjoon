N, C = map(int, input().split())
weight = list(map(int, input().split()))
front_arr = weight[:N//2]
back_arr = weight[N//2:]
front_part_sum = []
back_part_sum = []


def findPartSum(arr, sum_arr, now_weight, index):
    if index >= len(arr):
        sum_arr.append(now_weight)
        return
    findPartSum(arr, sum_arr, now_weight, index + 1)
    findPartSum(arr, sum_arr, now_weight + arr[index], index + 1)


def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    result = 0
    while end - start >= 0:
        mid = (start + end) // 2
        if arr[mid] <= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result + 1


findPartSum(front_arr, front_part_sum, 0, 0)
findPartSum(back_arr, back_part_sum, 0, 0)
back_part_sum.sort()

cnt = 0
for i in front_part_sum:
    if C - i >= 0:
        cnt += binarySearch(back_part_sum, C - i)
print(cnt)