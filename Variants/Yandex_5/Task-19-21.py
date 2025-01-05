def f(a, b, m, p):
    if a + b <= 42: return m % 2 == 0
    if m == 0: return 0
    h = []
    if p != '11': h += [f(a-4, b, m-1, '11')]
    if p != '21': h += [f(a, b - 4, m-1, '21')]
    if p != '12': h += [f(a//3, b, m-1, '12')]
    if p != '22': h += [f(a, b//3, m-1, '22')]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [b for b in range(2, 1000) if f(50, b, 2, '')])
print('20)', len([b for b in range(2, 1000) if not f(50, b, 1, '') and f(50, b, 3, '')]))
print('21)', [b for b in range(2, 1000) if not f(50, b, 2, '') and f(50, b, 4, '')])