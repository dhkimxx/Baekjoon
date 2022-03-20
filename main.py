L, P = map(int, input().split())
participant = list(map(int, input().split()))
for n in participant:
    print(n - L * P,end=" ")