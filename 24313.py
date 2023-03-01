a1, a2 = map(int, input().split())
c = int(input())
no = int(input())
if a1 * no + a2 <= c * no and a1 <= c:
    print(1)
else:
    print(0)