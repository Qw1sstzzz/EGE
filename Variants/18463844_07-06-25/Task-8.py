from itertools import product, repeat

alph = '01234567'
cnt = 0

for i in product(alph, repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('1') == 0 and len(set(s)) == len(s):
        for c in '0246':
            s = s.replace(c, '*')
        for c in '1357':
            s = s.replace(c, '!')
        if ('**' not in s) and ('!!' not in s):
            cnt += 1

print(cnt)