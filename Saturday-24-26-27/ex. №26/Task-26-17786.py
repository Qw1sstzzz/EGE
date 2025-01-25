with open('Task-26-17786-file.txt') as file:
    N, V = map(int, file.readline().split())
    data = [int(i) for i in file]

V = V * 1_000
ans, last = [], []

watermelons = sorted([i for i in data if 7000 <= i <= 12000], reverse=True)

mass = 0            # Прошлая масса арбузов
for i in watermelons:
    if i + mass <= V:       # Если предыдущая масса + новая <= Максимально возможной
        mass += i           # Обновляем использованную массу
        ans.append(i)

print(len(ans), ans[-1])

# 75 9196