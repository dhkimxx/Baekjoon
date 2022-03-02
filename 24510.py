Max = 0
for _ in range(int(input())):
    Code = input()
    count = Code.count('for') + Code.count('while')
    if count > Max: Max = count
print(Max)