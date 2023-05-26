K = int(input())
length = []
direction = []
max_width = 0
max_height = 0
for i in range(6):
    d, l = map(int, input().split())
    length.append(l)
    direction.append(d)
    if d == 1 or d == 2:
        if max_width < l:
            max_width = l
            max_width_index = i
    if d == 3 or d == 4:
        if max_height < l:
            max_height = l
            max_height_index = i

big_box = max_width * max_height
small_box_height = abs(length[(max_width_index - 1) % 6] - length[(max_width_index + 1) % 6])
small_box_width = abs(length[(max_height_index + 1) % 6] - length[(max_height_index - 1) % 6])
small_box = small_box_width * small_box_height
print(K * (big_box - small_box))
