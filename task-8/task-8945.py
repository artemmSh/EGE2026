from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:12], repeat=7):
    val = ''.join(val)
    if val[0] == '0' or any(val[i] == val[i + 1] for i in range(len(val) - 1)):
        continue
    flag = True
    # for i in val:
    #     if int(i) % 3 == 0:
    #         val = val.replace(i, '+')
    # for i in val:
    #     if int(i) % 3 != 0:
    #         val = val.replace(i, '-')
    # print(val)
    if val == '-+-+-+-' or val == '+-+-+-+':
        flag = False
    if flag:
        cnt += 1
    for i i
    val = [val.replace(i, '-') for i in '0369b']
    val = [val.replace(i, '+') for i in '124578a']
    print(val)
    # for i in [str(i) for i in range(12) if i % 3 == 0]:
    #     val.replace(i, '+')
    # for i in [str(i) for i in range(12) if i % 3]:
    #     val.replace(i, '-')
    # if val[0] != '0' and val == '-+-+-+-' or val == '+-+-+-+':
    #     cnt += 1
print(cnt)