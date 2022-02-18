Str = input()
sub = len(Str.split('-'))
add = len(Str.split('+'))
Num = Str.split('-')
Sum = []
for i in Num:
    Sum.append(sum(map(int, i.split('+'))))
result = Sum[0]
for i in range(1, len(Sum)):
    result -= Sum[i]
print(result)