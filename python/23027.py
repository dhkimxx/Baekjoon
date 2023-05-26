s = input()
if s.find('A') != -1:
    s = s.replace('B','A').replace('C','A').replace('D','A').replace('F','A')
elif s.find('B') != -1:
    s = s.replace('C','B').replace('D','B').replace('F','B')
elif s.find('C') != -1:
    s = s.replace('D','C').replace('F','C')
else:
    s = 'A' * len(s)
print(s)
