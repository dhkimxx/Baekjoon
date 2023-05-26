N = int(input())
arr = list(map(int, input().split()))
MIN = int(2e9)
candidate = (arr[0], arr[-1])

left = 0
right = N - 1

while left < right:
    if abs(arr[left] + arr[right]) <= MIN:
        MIN = abs(arr[left] + arr[right])
        candidate = (arr[left], arr[right])
    if arr[left] + arr[right] > 0:
        right -= 1
        continue
    elif arr[left] + arr[right] < 0:
        left += 1
        continue
    else:
        break
print(candidate[0], candidate[1])
