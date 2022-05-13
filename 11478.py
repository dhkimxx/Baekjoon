S = input()
s_list = []
for i in range(1, len(S) + 1):
    for j in range(0, len(S) - i + 1):
        s_list.append(S[j:j + i])
print(len(set(s_list)))
