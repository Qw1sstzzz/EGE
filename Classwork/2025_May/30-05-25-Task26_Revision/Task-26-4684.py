with open('Task-26-4684-file.txt') as f:
    N = int(f.readline())
    products = [int(i) for i in f]

products = sorted(products, reverse=True)

prices_for_consumer = sum(products) - sum(products[5::6]) / 2

products = sorted(products)
prices_for_market = sum(products) - sum(products[:N//6]) / 2

print(int(prices_for_consumer), int(prices_for_market))