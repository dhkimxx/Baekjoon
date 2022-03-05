list = [1,2,3,4,5,6,7,8,9,10]
sum = sum(l if l > 5 else 0 for l in list)
print(sum)