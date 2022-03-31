import heapq

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
            if N == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            if N == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])