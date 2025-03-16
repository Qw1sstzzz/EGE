def dell(num):
    r = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def f(arr1, arr2):
    cnt = 0
    for i in arr1:
        if i in arr2:
            cnt += 1
    return cnt

with open('Task-17-4329-file.txt') as file:
    data = [int(i) for i in file]

maxi = []
for i in data:
    divs = dell(i)
    maxi.append([len(divs), i])

maxi_divs = dell(max(maxi)[1])
ans = []

for i in range(len(data) - 1):
    p1, p2 = data[i], data[i+1]
    divs_1, divs_2 = dell(p1), dell(p2)
    u1 = f(divs_1, maxi_divs)
    u2 = f(divs_2, maxi_divs)
    if u1 >= 3 and u2 >= 3:
        ans.append(f(divs_1, divs_2))

print(len(ans), max(ans))