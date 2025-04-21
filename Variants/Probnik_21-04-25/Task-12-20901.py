s = '1' + '0'*90

while '1' in s:
    if '10' in s: s = s.replace('10', '0001', 1)
    else: s = s.replace('1', '000', 1)

print(s.count('0'))