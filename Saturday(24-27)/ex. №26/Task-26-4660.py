with open('Task-26-4660.txt') as file:
    N = int(file.readline().strip())
    data = [int(i) for i in file]

data, copy_data = sorted(data, key=lambda x: -x), sorted(data)

price_4_customer = sum([data[i] for i in range(3, len(data), 4)])
price_4_shop = sum([i for i in copy_data[:N//4]])

ans1 = sum(data) - price_4_customer + price_4_customer // 2
ans2 = sum(data) - price_4_shop + price_4_shop // 2

print(ans1, ans2, end='\n')

# 44101521 48825239