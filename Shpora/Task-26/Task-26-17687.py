with open('Task-26-17687-file.txt') as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data_for_customer = sorted(data, reverse=True)
ans_A = sum(data_for_customer) - sum(data_for_customer[:N//9])

data_for_shop = sorted(data, reverse=True)
ans_B = sum(data_for_shop) - sum(data_for_shop[8::9])

print(ans_A, ans_B)

