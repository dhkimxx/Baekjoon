import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0

def divide(length, graph):
    global white, blue
    if sum(map(sum, graph)) == 0:
        white += 1
        return
    if sum(map(sum, graph)) == length ** 2:
        blue += 1
        return
    quater = [[],[],[],[]]
    for i in range(0, length):
        if i < length // 2:
            quater[0].append(graph[i][length//2:])
            quater[1].append(graph[i][:length//2])
        else:
            quater[2].append(graph[i][length//2:])
            quater[3].append(graph[i][:length//2])
    for i in range(4):
        divide(length//2, quater[i])


divide(N, graph)
print(f"{white}\n{blue}")