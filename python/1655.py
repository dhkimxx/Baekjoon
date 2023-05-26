import sys
import heapq
N = int(sys.stdin.readline())
maxHeap = []
minHeap = []

mid = int(sys.stdin.readline())
print(mid)
for n in range(2, N + 1):
    x = int(sys.stdin.readline())
    if mid < x:
        heapq.heappush(minHeap, x)
    else:
        heapq.heappush(maxHeap, -x)

    if len(minHeap) - len(maxHeap) == 2:
        heapq.heappush(maxHeap, -mid)
        mid = heapq.heappop(minHeap)
    if len(maxHeap) - len(minHeap) == 2:
        heapq.heappush(minHeap, mid)
        mid = -heapq.heappop(maxHeap)

    if len(maxHeap) <= len(minHeap):
        print(mid)
    if len(maxHeap) > len(minHeap):
        print(-maxHeap[0])
'''
import sys
import heapq

N = int(sys.stdin.readline())
maxHeap = []
minHeap = []

mid = int(sys.stdin.readline())
print(mid)

for n in range(2, N + 1):
    x = int(sys.stdin.readline())
    if mid <= x:
        heapq.heappush(minHeap, x)
        if len(minHeap) - len(maxHeap) == 2:
            heapq.heappush(maxHeap, -mid)
            mid = heapq.heappop(minHeap)
    
    if mid > x:
        heapq.heappush(maxHeap, -x)
        if len(maxHeap) - len(minHeap) == 2:
            heapq.heappush(minHeap, mid)
            mid = -heapq.heappop(maxHeap)
            
    if len(maxHeap) <= len(minHeap):
        print(mid)
    if len(maxHeap) > len(minHeap):
        print(-maxHeap[0])
'''