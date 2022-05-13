N_A, N_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dict_A = {a: 1 for a in A}
dict_B = {b: 1 for b in B}
ans = N_A + N_B
for a in A:
    if dict_B.get(a, 0):
        ans -= 1
for b in B:
    if dict_A.get(b, 0):
        ans -= 1
print(ans)