with open('Task-17-21712-file.txt') as f:
    data = [int(i) for i in f]

mini_pos = min([i for i in data if len(str(abs(i))) == 4 and str(i)[-1] == '6' and i > 0])
ans = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i:i+3]
    u1 = len(str(abs(p1))) == 4 and str(p1)[-1] == '6'
    u2 = len(str(abs(p2))) == 4 and str(p2)[-1] == '6'
    u3 = len(str(abs(p3))) == 4 and str(p3)[-1] == '6'
    if u1 + u2 + u3 == 1:
        if p1 + p2 + p3 <= mini_pos:
            ans.append(p1 + p2 + p3)
print(len(ans), max(ans))