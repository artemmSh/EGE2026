from string import printable as alph
from itertools import *
from math import sqrt
cnt = 0
for val in product(alph[:16], repeat=5):
    val = ''.join(val)
    if all(val.count(i)<=2 for i in val):
        cnt = 0
        for i in val:
            if sqrt(i) ==