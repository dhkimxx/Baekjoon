import sys
N = int(sys.stdin.readline())
A = list(sys.stdin.readline().split())
stack = [A[0]]
NGE = [-1 for i in range(N)]
j = 0
for i in range(N):
    if stack[-1] < A[i]:
        for k in range(j, i):
            if A[k] < A[i]:
                NGE[k] = A[i]
        stack = [A[i]]
        j = i
    else:
        stack.append(A[i])

for n in range(len(NGE)):
    print(NGE[n], end=' ')
