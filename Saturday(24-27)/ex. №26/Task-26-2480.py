file = open('Task-26-2480-file.txt')
N = int(file.readline())

road = [0] * 2_000_000

for i in range(N):
    start, end = map(int, file.readline().split())
    road[start] += 1
    road[end] -= 1
# Отмечаем все отрезки начала и конца жалоб

st, end = -1, 0
count, length = 0, 0
k = 0 # Количество жалоб на участок дороги
for i in range(2_000_000):
    k0 = k
    k += road[i]
    if k > 0 and st == -1:
        st = i
    if k == 0 and k0 > 0:
        end = i
        length += end - st
        count += 1
        st, end = -1, 0

print(count, length)