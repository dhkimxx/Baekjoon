N, M = map(int, input().split())
Pokedex = {}
for i in range(1, N + 1):
    temp = input()
    Pokedex[temp] = i
    Pokedex[str(i)] = temp
for _ in range(M):
    print(Pokedex[input()])