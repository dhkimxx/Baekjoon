A, B = map(int, input().split())
arr = [0, 1]
for i in range(2, B + 1):
    for _ in range(i):
        arr.append(i)
for n in range(1, len(arr)):
    arr[n] += arr[n - 1]
print(arr[B] - arr[A - 1])
