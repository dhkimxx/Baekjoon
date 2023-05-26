from collections import deque
import sys
while 1:
    deq = deque()
    Q = list(sys.stdin.readline())[:-1]
    if Q == ['.']:
        break
    result = "yes"
    for q in Q:
        if q == '(' or q == '[':
            deq.append(q)
        elif q == ')':
            if len(deq) == 0:
                result = "no"
                break
            elif deq[-1] == '(':
                deq.pop()
            else:
                result = "no"
                break
        elif q == ']':
            if len(deq) == 0:
                result = "no"
                break
            elif deq[-1] == '[':
                deq.pop()
            else:
                result = "no"
                break
    if len(deq):
        result = "no"
    print(result)