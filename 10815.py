import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
dictionary = {card: 1 for card in cards}
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if dictionary.get(target, 0):
        print(1, end=' ')
    else:
        print(0, end=' ')

'''
import sys
input = sys.stdin.readline

card = [0] * 20000001
N = int(input())
card1 = list(map(int, input().split()))
for i in card1:
    card[i + 10000001] = 1

M = int(input())
card2 = list(map(int, input().split()))
for i in card2:
    if card[i + 10000001]:
        print(1, end=' ')
    else:
        print(0, end=' ')
'''
'''
import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
card_target = list(map(int, input().split()))

for target in card_target:
    start = 0
    end = N - 1
    while 1:
        mid = (start + end) // 2
        if card[mid] == target:
            print(1, end=' ')
            break
        if card[mid] < target:
            start = mid + 1
        if card[mid] > target:
            end = mid - 1
        if start > end:
            print(0, end=' ')
            break
'''