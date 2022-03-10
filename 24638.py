firstYear, secondYear = list(input().split()), list(input(). split())
if firstYear[0] == 'AD' and secondYear[0] == 'AD':
    print(abs(int(firstYear[1]) - int(secondYear[1])))
if firstYear[1] == 'BC' and secondYear[0] == 'AD':
    print(int(firstYear[0]) + int(secondYear[1]) - 1)
if firstYear[0] == 'AD' and secondYear[1] == 'BC':
    print(int(firstYear[1]) + int(secondYear[0]) - 1)
if firstYear[1] == 'BC' and secondYear[1] == 'BC':
    print(abs(int(firstYear[0]) - int(secondYear[0])))
