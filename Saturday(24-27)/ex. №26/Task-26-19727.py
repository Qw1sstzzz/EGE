with open('Task-26-19727-file.txt') as file:
    M, N = map(int, file.readline().split())
    data = [int(i) for i in file]

data = sorted(data)
bidons = []
last = []

for i in data:
    if i <= M:
        bidons.append(i)
        M -= i
    # Проверка, что ещё можно загрузить бидон в контейнер

    else:
        l = last[-1]        # Последняя i, которую мы использовали + полученная масса, меньшая допустимому
        M += l
        break
    last.append(i)          # Фиксируем наши массы

ans_A = len(bidons)
ans_B = len([int(i) for i in data if i > M])
print(ans_A, ans_B)

# 162 788