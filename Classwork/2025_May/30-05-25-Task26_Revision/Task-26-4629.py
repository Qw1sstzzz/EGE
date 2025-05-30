with open('Task-26-4629-file.txt') as f:
    N = int(f.readline())
    products = [int(i) for i in f]

products = sorted(products, reverse=True)
price_for_customer = sum(products) - sum(products[:N // 4]) / 2

products = sorted(products)
price_for_market = sum(products) - sum(products[:N // 4]) / 2

print(int(price_for_customer), int(price_for_market))

