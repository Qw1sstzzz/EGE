with open('Task-26-4660-file.txt') as f:
    N = int(f.readline())
    products = [int(i) for i in f]

products = sorted(products)

price_for_client = sum(products) - sum(products[::4]) / 2

products = sorted(products)
price_for_market = sum(products) - sum(products[:N // 4]) / 2


print(int(price_for_client), int(price_for_market))

