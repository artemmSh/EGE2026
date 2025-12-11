from itertools import product
import time

start = time.time()
cnt = 0
for val in product('01234567', repeat=10):
    val = ''.join(val)
    if val.count('7') != 5 or val[0] == '0':
        continue
    flag = True
    for i in range(len(val) - 1):
        a, b = val[i], val[i + 1]
        if (a == '7' and b in '1357') or (b == '7' and a in '1357'):
            flag = False
    if flag:
        cnt += 1
print(cnt)
end = time.time()
print(f'Time:{end - start}')
