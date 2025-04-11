def f(x, m, sh = ''):
    if x > 40: return m % 2 == 0
    if m == 0: return 0
    h = []
    if sh == '1':
        h = [f(x+6, m-1, '2'), f(x*2, m-1, '3')]
    if sh == '2':
        h = [f(x+3, m-1, '1'), f(x*2, m-1, '3')]
    if sh == '3':
        h = [f(x+3, m-1, '1'), f(x+6, m-1, '2')]
    if sh == '':
        h = [f(x+3, m-1, '1'), f(x+6, m-1, '2'), f(x*2, m-1, '3')]
    return any(h) if m % 2 != 0 else all(h)

print('19)', max([s for s in range(2, 37) if f(s, 2, '')]))
print('20)', max([s for s in range(2, 37) if not f(s, 1, '') and f(s, 3, '')]))
print('21)', *([s for s in range(2, 37) if not f(s, 2, '') and f(s, 4, '')]))