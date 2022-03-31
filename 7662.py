import heapq


def synchro(heap):
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)


for _ in range(int(input())):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * k

    for key in range(k):
        Q, N = input().split()
        if Q == 'I':
            heapq.heappush(min_heap, (int(N), key))
            heapq.heappush(max_heap, (-int(N), key))
            visited[key] = True
        if Q == 'D':
            if N == '1' and max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
            if N == '-1' and min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
        synchro(max_heap)
        synchro(min_heap)
    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])
