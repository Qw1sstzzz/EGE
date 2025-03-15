with open('Task-26-Krylov25-1Var-file.txt.txt') as file:
    N, M, K = map(int, file.readline().split())
    ships = [list(map(int, i.split())) for i in file]

