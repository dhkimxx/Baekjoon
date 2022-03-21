N = input()
startBinary = ["0","1","10","11","100","101","110","111"]
binary = ["000","001","010","011","100","101","110","111"]
print(startBinary[int(N[0])], end="")
for n in N[1:]:
    print(binary[int(n)], end="")