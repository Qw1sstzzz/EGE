with open('Task-26-6759-file.txt') as f:
    N = int(f.readline())
    data = [int(i) for i in f]

products_for_customer = sorted(data, reverse=True)
ans_A = sum(products_for_customer) - sum(products_for_customer[:N//3])

ans_B = sum(products_for_customer) - sum(products_for_customer[2::3])
print(ans_A, ans_B)