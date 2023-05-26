graph = []
known = [[] for _ in range(10)]
for i in range(9):
    graph.append(list(map(int, input().replace('.', '0'))))
    for j in range(9):
        known[graph[i][j]].append((i, j))


def print_graph():
    for i in range(9):
        print(''.join(map(str, graph[i])).replace('0', '.'))


def complete_check():
    SUM = 0
    for a in range(0, 9):
        for b in range(0, 9):
            SUM += graph[a][b]
    if SUM == 405:
        print_graph()
        exit()


while 1:
    loop_stop_flag = 1
    for n in range(1, 10):
        candidates_x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        candidates_y = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i, j in known[n]:
            if i in candidates_x:
                candidates_x.remove(i)
            if j in candidates_y:
                candidates_y.remove(j)
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                box_pass_flag = 0
                candidates_cnt = 0
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if graph[i][j] == n:
                            box_pass_flag = 1
                        if i in candidates_x and j in candidates_y:
                            if graph[i][j] == 0:
                                candidates_cnt += 1
                                temp_x, temp_y = i, j
                if box_pass_flag:
                    continue
                if candidates_cnt == 1:
                    loop_stop_flag = 0
                    graph[temp_x][temp_y] = n
                    candidates_x.remove(temp_x)
                    candidates_y.remove(temp_y)
                    known[n].append((temp_x, temp_y))
                    complete_check()
                if candidates_cnt == 0:
                    print('ERROR')
                    exit()
    if loop_stop_flag == 1:
        print_graph()
        break
